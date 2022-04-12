# -*- coding: utf-8 -*-
"""This module is responsible for the model evaluation, metrics extraction, and
plots."""
import json
import argparse
import configparser
import math
import sys
from pathlib import Path
import joblib
import yaml

from sklearn.metrics import (
    roc_curve,
    precision_recall_curve,
    accuracy_score,
    average_precision_score,
    roc_auc_score,
    brier_score_loss,
    matthews_corrcoef,
    f1_score,
)

PARAMS_FILE = "params.yaml"


def main(
    input_folder, model_folder, scores_file, prc_file, roc_file, cfm_file
):
    """Evaluating the model."""

    with open(PARAMS_FILE, "r", encoding="utf-8") as file:
        params = yaml.load(file, Loader=yaml.SafeLoader)
        target = params["dataset"]["target"]

    # Path to the featurized test.joblib dataset
    test_in_path = Path(f"{input_folder}/test.joblib").resolve()

    # Path to the model
    model_path = Path(f"{model_folder}/model.joblib").resolve()

    # Load the featurized data
    test = joblib.load(test_in_path)

    X_test, y_test = (
        test.drop(target, axis=1),
        test.pop(target),
    )

    # Load the model
    model = joblib.load(model_path)

    # Make predictions
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]

    # Accuracy
    acc = accuracy_score(y_test, y_pred)

    # F1-score
    f1 = f1_score(y_test, y_pred)

    # Brier Score
    brier = brier_score_loss(y_test, y_pred_proba)

    # Matthews Correlation Coefficient
    matthews = matthews_corrcoef(y_test, y_pred)

    # ROC curve and metrics
    fpr, tpr, roc_thresholds = roc_curve(y_test, y_pred_proba)
    roc_auc = roc_auc_score(y_test, y_pred_proba)

    # PRC curve and metrics
    precision, recall, prc_thresholds = precision_recall_curve(
        y_test, y_pred_proba
    )
    avg_prec = average_precision_score(y_test, y_pred_proba)

    # Create scores.json file
    with open(scores_file, "w", encoding="utf-8") as fd:
        json.dump(
            {
                "Avg Precision": avg_prec,
                "ROC_AUC": roc_auc,
                "Accuracy": acc,
                "Brier score": brier,
                "MCC (Matthews)": matthews,
                "F1-score": f1,
            },
            fd,
            indent=4,
        )

    ## Create the prc.json
    # Decreases the number of points of the PRC curve
    nth_point = math.ceil(len(prc_thresholds) / 1000)
    prc_points = list(zip(precision, recall, prc_thresholds))[::nth_point]
    with open(prc_file, "w", encoding="utf-8") as fd:
        json.dump(
            {
                "prc": [
                    {"precision": p, "recall": r, "threshold": t}
                    for p, r, t in prc_points
                ]
            },
            fd,
            indent=4,
        )

    # Create the roc.json
    with open(roc_file, "w", encoding="utf-8") as fd:
        json.dump(
            {
                "roc": [
                    {"fpr": fp, "tpr": tp, "threshold": t}
                    for fp, tp, t in zip(fpr, tpr, roc_thresholds)
                ]
            },
            fd,
            indent=4,
        )

    with open(cfm_file, "w", encoding="utf-8") as fd:
        json.dump(
            {
                "cfm": [
                    {"actual": int(actual), "predicted": int(pred)}
                    for actual, pred in zip(
                        y_test.values.ravel(), y_pred_proba.round()
                    )
                ]
            },
            fd,
            indent=4,
        )

    sys.exit(0)


if __name__ == "__main__":

    # Parse arguments from configs.ini file
    config = configparser.ConfigParser()
    config.read("configs.ini")

    # Convert to pathlib objects
    processed_folder = Path(config["datasets"]["processed_folder"]).resolve()
    models_folder = Path(config["datasets"]["models_folder"]).resolve()
    reports_folder = Path(config["datasets"]["reports_folder"]).resolve()

    # Parse arguments from the command line
    parser = argparse.ArgumentParser(
        description="Evaluate the model and create the plots"
    )
    parser.add_argument(
        "-i",
        "--input_folder",
        type=Path,
        default=processed_folder,
        help="Folder where the featurized test dataset is located",
    )
    parser.add_argument(
        "-m",
        "--model_folder",
        type=Path,
        default=models_folder,
        help="Folder where the model is located",
    )
    parser.add_argument(
        "-s",
        "--scores_file",
        type=str,
        default=reports_folder / "scores.json",
        help="File where the scores will be saved",
    )
    parser.add_argument(
        "-p",
        "--prc_file",
        type=str,
        default=reports_folder / "prc.json",
        help="File where the PRC curve will be saved",
    )
    parser.add_argument(
        "-r",
        "--roc_file",
        type=str,
        default=reports_folder / "roc.json",
        help="File where the ROC curve will be saved",
    )
    parser.add_argument(
        "-c",
        "--cfm_file",
        type=str,
        default=reports_folder / "cfm.json",
        help="File where the confusion matrix will be saved",
    )
    args = parser.parse_args()

    # Call the main function
    main(**vars(args))
