# -*- coding: utf-8 -*-
"""This module is responsible by the model creation and model training."""
import argparse
from pathlib import Path
from sklearn.ensemble import (
    RandomForestClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier,
)
import joblib
import yaml


def train(input_folder, model_folder):

    with open("params.yaml", "r", encoding="utf-8") as file:
        params = yaml.load(file, Loader=yaml.SafeLoader)
        target = params["dataset"]["target"]
        clf = params["train"]["clf"]
        clf_params = params["train"]["clf_params"]

    # Path to the featurized train.joblib dataset
    train_in_path = Path(f"{input_folder}/train.joblib").resolve()

    # Path where the trained model will be stored
    model_out_path = Path(f"{model_folder}/model.joblib").resolve()

    # Load the featurized data
    train = joblib.load(train_in_path)

    # Split the data into features and target
    X_train, y_train = (
        train.drop(target, axis=1),
        train.pop(target),
    )

    # Dictionary of classifiers
    classifiers = {
        "RandomForestClassifier": RandomForestClassifier,
        "AdaBoostClassifier": AdaBoostClassifier,
        "GradientBoostingClassifier": GradientBoostingClassifier,
    }

    # If the classifier is not in the dictionary, exit with error
    if clf not in classifiers.keys():
        raise ValueError(f"Classifier {clf} not found.")

    ## Verify if all parameters passed by the yaml are valid
    ## classifier parameters
    attributes = dir(classifiers[clf]())
    invalid_arg = [arg for arg in clf_params if arg not in attributes]

    # If there are invalid parameters, print an error message and exit
    if invalid_arg:
        raise ValueError(f"Error: Invalid parameters {invalid_arg}")

    # Instantiate the classifier
    model = classifiers[clf](**clf_params)

    # Train the model
    model.fit(X_train, y_train.values.ravel())

    # Save the model
    joblib.dump(model, model_out_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train a model using the featurized data."
    )
    parser.add_argument(
        "-i",
        "--input_folder",
        type=str,
        help="Path to the input folder containing the featurized data.",
    )
    parser.add_argument(
        "-m",
        "--model_folder",
        type=str,
        help="Path to the folder where the models will be stored.",
    )
    args = parser.parse_args()
    train(**vars(args))
