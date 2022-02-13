# -*- coding: utf-8 -*-
import sys
import os
from pathlib import Path
import joblib
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
import yaml

# Test if the required parameters are received
if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write(
        "\tpython3 src/features/build_features.py prepared-dir-path"
        " features-dir-path\n"
    )
    sys.exit(1)

with open("params.yaml") as file:
    params = yaml.load(file, Loader=yaml.SafeLoader)
    target = params["dataset"]["target"]
    ohe_cols = params["featurize"]["ohe_cols"]

# Configure Paths and Folders
input_folder, output_folder = sys.argv[1:]

# If doesn't exist, create the output data folder
os.makedirs(output_folder, exist_ok=True)

# Path to cleaned train.csv and test.csv datasets
train_in_path = Path(f"{input_folder}/train.csv").resolve()
test_in_path = Path(f"{input_folder}/test.csv").resolve()

# The resulting data of the featurization process will
# be stored according to the paths defined below
train_out_path = Path(f"{output_folder}/train.joblib").resolve()
test_out_path = Path(f"{output_folder}/test.joblib").resolve()
pipeline_out_path = Path(f"{output_folder}/featurize.joblib").resolve()


# Load the preprocessed data
train = pd.read_csv(train_in_path, index_col=[0])
test = pd.read_csv(test_in_path, index_col=[0])

X_train, y_train = (
    train.drop(target, axis=1),
    train[[target]],
)


X_test, y_test = (
    test.drop(target, axis=1),
    test[[target]],
)

# ======= Featurization Pipeline =========

ohe = make_pipeline(
    OneHotEncoder(handle_unknown="ignore", sparse=False),
)
featurize = make_column_transformer(
    (ohe, ohe_cols),
    verbose_feature_names_out=False,
)

# ========================================


# Fit & Transform the selected columns, then rebuild the DataFrame
featurize.fit(X_train)

cols = featurize.get_feature_names_out()

X_train = pd.DataFrame(
    featurize.transform(X_train), index=X_train.index, columns=cols
)
X_test = pd.DataFrame(
    featurize.transform(X_test), index=X_test.index, columns=cols
)

# Rebuild the dataset with features + target
train_out = pd.concat([X_train, y_train], axis=1)
test_out = pd.concat([X_test, y_test], axis=1)

# Save the resulted datasets
joblib.dump(train_out, train_out_path)
joblib.dump(test_out, test_out_path)

# Save the pipeline
joblib.dump(featurize, pipeline_out_path)
