# -*- coding: utf-8 -*-
"""This module is responsible for clean, fill and fix data."""
import sys
import os
from pathlib import Path
import joblib
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

import yaml

# Test if the required parameters are received
if len(sys.argv) != 4:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write(
        "\tpython3 src/prepare/prepare_dataset.py data-dir-path"
        " features-dir-path"
        " model-path-dir\n"
    )
    sys.exit(1)

with open("params.yaml", "r", encoding="utf-8") as file:
    params = yaml.load(file, Loader=yaml.SafeLoader)
    target = params["dataset"]["target"]
    prepare = params["prepare"]
    random_state = params["prepare"]["random_state"]
    split = params["prepare"]["split"]
    cat_missing = params["prepare"]["missing"]["cat_cols"]
    num_missing = params["prepare"]["missing"]["num_cols"]
    drop_cols = params["prepare"]["drop"]["cols"]


# Save the input and output paths received as parameter
input_folder, output_folder, model_folder = sys.argv[1], sys.argv[2], sys.argv[3]

# If doesn't exist, create the output data folder
os.makedirs(output_folder, exist_ok=True)

# Path to the raw train.csv.This data will be splitted
# into train and test. Then the transformations will be
# applyed.
data_path = Path(f"{input_folder}/train.csv").resolve()

# The resulting data of the preprocessing will be store
# on the folder define by the paths below. Also store the
# pipeline object as .joblib
train_out_path = Path(f"{output_folder}/train.csv").resolve()
test_out_path = Path(f"{output_folder}/test.csv").resolve()
pipeline_out_path = Path(f"{model_folder}/pre_processing.joblib").resolve()


# Load data and split in train and test
data = pd.read_csv(data_path, index_col=[0])

# Separe the predictors from the target variable
X, y = (
    data.drop(target, axis=1),
    data[[target]],
)

# Split into train/test data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=split, random_state=random_state
)

# ======= Pre-processing Pipeline =========

num_imputer = make_pipeline(
    SimpleImputer(strategy="constant", fill_value=0),
)

cat_imputer = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="None"),
)


pre_processing = make_column_transformer(
    (num_imputer, num_missing),
    (cat_imputer, cat_missing),
)

# =========================================

# Fit & Transform selected columns
pre_processing.fit(X_train)

# Make sure to update only the selected columns,
# and in the same order
X_train[num_missing + cat_missing] = pre_processing.transform(X_train)
X_test[num_missing + cat_missing] = pre_processing.transform(X_test)

# Because the SimpleImputer() doesn't implement the
# 'get_features_names_out()' the columns defined in
# 'drop_cols' variable will be dropped manually.
# This will avoid unnecessary step to rebuild the
# dataframe columns
X_train = X_train.drop(drop_cols, axis=1)
X_test = X_test.drop(drop_cols, axis=1)

# Rebuild the dataset with features + target
train_out = pd.concat([X_train, y_train], axis=1)
test_out = pd.concat([X_test, y_test], axis=1)

# Save the resulted datasets
train_out.to_csv(train_out_path)
test_out.to_csv(test_out_path)

# Save the pipeline
joblib.dump(pre_processing, pipeline_out_path)
