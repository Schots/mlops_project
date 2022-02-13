# -*- coding: utf-8 -*-
import sys
import os
from pathlib import Path
import joblib
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
import yaml

if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write(
        "\tpython3 src/model/train_model.py processed-dir-path"
        " model-dir-path\n"
    )
    sys.exit(1)

with open("params.yaml") as file:
    params = yaml.load(file, Loader=yaml.SafeLoader)
    target = params["dataset"]["target"]
    seed = params["train"]["seed"]
    n_estimators = params["train"]["n_estimators"]
    min_split = params["train"]["min_split"]
    n_jobs = params["train"]["n_jobs"]

# Configure Paths and Folders
input_folder, output_folder = sys.argv[1:]

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
