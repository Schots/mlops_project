# -*- coding: utf-8 -*-
"""This module is responsible by the model creation and model training."""
import sys
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
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
    seed = params["train"]["seed"]
    n_estimators = params["train"]["n_estimators"]
    min_split = params["train"]["min_split"]
    n_jobs = params["train"]["n_jobs"]

# Configure Paths and Folders
input_folder, output_folder = sys.argv[1], sys.argv[2]

# Path to the featurized train.joblib dataset
train_in_path = Path(f"{input_folder}/train.joblib").resolve()

# Path where the trained model will be stored
model_out_path = Path(f"{output_folder}/model.joblib").resolve()

# Load the featurized data
train = joblib.load(train_in_path)

X_train, y_train = (
    train.drop(target, axis=1),
    train[[target]],
)

# ==== Build the Model ==========

model = RandomForestClassifier(
    n_estimators=n_estimators,
    min_samples_split=min_split,
    n_jobs=n_jobs,
    random_state=seed,
)

# ==============================

# Train the model
model.fit(X_train, y_train.values.ravel())

# Save the model
joblib.dump(model, model_out_path)
