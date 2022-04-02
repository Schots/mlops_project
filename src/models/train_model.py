# -*- coding: utf-8 -*-
"""This module is responsible by the model creation and model training."""
import sys
from pathlib import Path
from sklearn.ensemble import (
    RandomForestClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier,
)
import joblib
import yaml

if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write(
        "\tpython3 src/models/train_model.py processed-dir-path"
        " model-dir-path\n"
    )
    sys.exit(1)

with open("params.yaml", "r", encoding="utf-8") as file:
    params = yaml.load(file, Loader=yaml.SafeLoader)
    target = params["dataset"]["target"]
    clf = params["train"]["clf"]
    clf_params = params["train"]["clf_params"]

# Configure Paths and Folders
input_folder, model_folder = sys.argv[1], sys.argv[2]

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
    print(f"Error: {classifiers[clf].__name__} is not a supported classifier.")
    sys.exit(1)

## Verify if all parameters passed by the yaml are valid
## classifier parameters
attributes = dir(classifiers[clf]())
invalid_arg = [arg for arg in clf_params if arg not in attributes]

# If there are invalid parameters, print an error message and exit
if invalid_arg:
    print(
        f"Error: {classifiers[clf].__name__} invalid parameters {invalid_arg}"
    )
    sys.exit(1)

# Instantiate the classifier
model = classifiers[clf](**clf_params)

# Train the model
model.fit(X_train, y_train.values.ravel())

# Save the model
joblib.dump(model, model_out_path)
