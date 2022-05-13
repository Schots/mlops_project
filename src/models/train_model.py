# -*- coding: utf-8 -*-
"""This module is responsible by the model creation and model training."""
import argparse
from pathlib import Path
from collections import namedtuple
from sklearn.base import ClassifierMixin
from sklearn.utils import all_estimators
import joblib
import yaml


__all_classifiers = {
    name: obj
    for name, obj in all_estimators()
    if issubclass(obj, ClassifierMixin)
}
Classifiers = namedtuple("Classifiers", __all_classifiers.keys())(
    *__all_classifiers.values()
)


def train(input_folder, model_folder, params=None):
    if params is None:
        with open("params.yaml", "r", encoding="utf-8") as file:
            params = yaml.load(file, Loader=yaml.SafeLoader)

    target = params["dataset"]["target"]
    clf = params["train"]["clf"]
    clf_params = params["train"]["clf_params"]

    # If the classifier is not in the dictionary, exit with error
    if clf not in __all_classifiers.keys():
        raise ValueError(f"Classifier {clf} not found.")

    classifier = getattr(Classifiers, clf)
    ## Verify if all parameters passed by the yaml are valid
    ## classifier parameters
    attributes = dir(classifier())
    invalid_arg = [arg for arg in clf_params if arg not in attributes]

    # If there are invalid parameters, print an error message and exit
    if invalid_arg:
        raise ValueError(f"Error: Invalid parameters {invalid_arg}")

    # Path to the featurized train.joblib dataset
    train_in_path = Path(f"{input_folder}/train.joblib").resolve()

    # Path where the trained model will be stored
    model_out_path = Path(f"{model_folder}/model.joblib").resolve()

    # Load the featurized data
    train_data = joblib.load(train_in_path)

    # Split the data into features and target
    X_train, y_train = (
        train_data.drop(target, axis=1),
        train_data.pop(target),
    )

    # Instantiate the classifier
    model = classifier(**clf_params)

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
