# -*- coding: utf-8 -*-
"""This module is responsible by the model creation and model training."""
import sys
import argparse
import configparser
from pathlib import Path
from sklearn.ensemble import (
    RandomForestClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier,
)
import joblib
import yaml

PARAMS_FILE = "params.yaml"


def main(input_folder, model_folder):
    """Function to train the model."""

    with open(PARAMS_FILE, "r", encoding="utf-8") as file:
        params = yaml.load(file, Loader=yaml.SafeLoader)
        target = params["dataset"]["target"]
        clf = params["train"]["clf"]
        clf_params = params["train"]["clf_params"]

    # Path to the featurized train.joblib dataset
    train_in_path = Path(input_folder) / "train.joblib"

    # Path where the trained model will be stored
    model_out_path = Path(model_folder) / "model.joblib"

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
        print(
            f"Error: {classifiers[clf].__name__} is not a supported"
            " classifier."
        )
        sys.exit(1)

    ## Verify if all parameters passed by the yaml are valid
    ## classifier parameters
    attributes = dir(classifiers[clf]())
    invalid_arg = [arg for arg in clf_params if arg not in attributes]

    # If there are invalid parameters, print an error message and exit
    if invalid_arg:
        print(
            f"Error: {classifiers[clf].__name__} invalid parameters"
            f" {invalid_arg}"
        )
        sys.exit(1)

    # Instantiate the classifier
    model = classifiers[clf](**clf_params)

    # Train the model
    model.fit(X_train, y_train.values.ravel())

    # Save the model
    joblib.dump(model, model_out_path)

    sys.exit(0)


if __name__ == "__main__":

    # Parse arguments from configs.ini file
    config = configparser.ConfigParser()
    config.read("configs.ini")

    # Convert to pathlib objects
    processed_folder = Path(config["datasets"]["processed_folder"]).resolve()
    models_folder = Path(config["datasets"]["models_folder"]).resolve()

    # Parse arguments from the command line
    parser = argparse.ArgumentParser(
        description="Train a model using the features."
    )
    parser.add_argument(
        "-i",
        "--input_folder",
        type=Path,
        default=processed_folder,
        help="Path to the input folder containing the features.",
    )
    parser.add_argument(
        "-m",
        "--model_folder",
        type=Path,
        default=models_folder,
        help="Path to the folder where the models will be stored.",
    )

    args = parser.parse_args()

    # Call the main function
    main(**vars(args))
