# -*- coding: utf-8 -*-
"""This module is responsible for the model evaluation, metrics extraction, and
plots."""
import json
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
)

if len(sys.argv) != 7:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write(
        "\tpython src/model/evaluate_model.py model features scores prc roc"
        " cfm\n"
    )
    sys.exit(1)

with open("params.yaml", "r", encoding="utf-8") as file:
    params = yaml.load(file, Loader=yaml.SafeLoader)
    target = params["dataset"]["target"]


input_folder, model_folder, scores_file, prc_file, roc_file, cfm_file = (
    sys.argv[1],
    sys.argv[2],
    sys.argv[3],
    sys.argv[4],
    sys.argv[5],
    sys.argv[6],
)

# Path to the featurized test.joblib dataset
test_in_path = Path(f"{input_folder}/test.joblib").resolve()

# Path to the model
model_path = Path(f"{model_folder}/model.joblib").resolve()

# Load the featurized data
test = joblib.load(test_in_path)

X_test, y_test = (
    test.drop(target, axis=1),
    test[[target]],
)

# Load the model
model = joblib.load(model_path)

# Make predictions
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

print(y_pred)

# Accuracy
acc = accuracy_score(y_test, y_pred)

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
        {"avg_prec": avg_prec, "roc_auc": roc_auc, "acc": acc}, fd, indent=4
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
