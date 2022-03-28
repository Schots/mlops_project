# -*- coding: utf-8 -*-
"""This module is responsible for feature engineering such as normalization,
standardization, encoding, etc."""
import sys
import os
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sklearn.pipeline import make_pipeline, make_union
from sklearn.compose import make_column_transformer, make_column_selector
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import FunctionTransformer
from custom_transformers import (
    count_features,
    discretize_feature,
    boolean_feature,
    extract_titles,
)

import yaml

# Test if the required parameters were received
# If not, exit the program
# At least 3 parameters are expected (excluding the script name):
# 1. The path to the raw data.
# 2. The path to the output data.
# 3. The path to store the models.
if len(sys.argv) != 4:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write(
        "\tpython3 src/features/build_features.py raw-dir-path"
        " features-dir-path"
        " model-dir-path\n"
    )
    sys.exit(1)

# Open the configuration file. All the parameters are stored in the params.yaml file.
# In this file the user can specify the parameters for the feature engineering, such as
# the target, the preprocess steps, feature creation, feature selection, etc.
with open("params.yaml", "r", encoding="utf-8") as file:
    # Load the entire file
    params = yaml.load(file, Loader=yaml.SafeLoader)

    # Find the target (y variable) in the file.
    target = params["dataset"]["target"]

    # Find the preprocess steps in the file.
    prepare = params["prepare"]
    random_state = prepare["random_state"]
    split = prepare["split"]
    stratify = prepare["stratify"]

    cat_missing = prepare["missing"]["categorical"]
    num_missing = prepare["missing"]["numerical"]

    # Find the feature creation steps in the file.
    featurize = params["featurize"]
    count_feat = featurize["count"]
    discretize_feat = featurize["discretize"]
    boolean_feat = featurize["boolean"]
    title_feat = featurize["title"]

# Read the parameters received from the command line
input_folder, output_folder, model_folder = (
    sys.argv[1],
    sys.argv[2],
    sys.argv[3],
)

# If doesn't exist, create the output data folder
os.makedirs(output_folder, exist_ok=True)

# Path to raw train.csv and test.csv data sets
data_path = Path(f"{input_folder}/train.csv").resolve()

# The resulting data of the featurization process will
# be stored according to the following paths
train_out_path = Path(f"{output_folder}/train.joblib").resolve()
test_out_path = Path(f"{output_folder}/test.joblib").resolve()
pipeline_out_path = Path(f"{model_folder}/featurize.joblib").resolve()

# Load raw data and split in train and test
data = pd.read_csv(data_path, index_col=[0])

# Split the predictors and the target
X, y = (
    data.drop(target, axis=1),
    data[[target]],
)


# Split into train/test data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=split, random_state=random_state, stratify=y
)


# ======= Pre-processing Pipeline =========

pre_processing = make_column_transformer(
    (SimpleImputer(strategy="median"), num_missing),
    (
        make_pipeline(
            SimpleImputer(strategy="most_frequent"),
            OneHotEncoder(handle_unknown="ignore", sparse=False),
        ),
        cat_missing,
    ),
)


# ======= Featurization Pipeline =========

featurize = make_column_transformer(
    (FunctionTransformer(count_features, kw_args={"offset": 1}), count_feat),
    (FunctionTransformer(boolean_feature), boolean_feat),
    (
        FunctionTransformer(discretize_feature, kw_args={"quantiles": 4}),
        discretize_feat,
    ),
    (
        make_pipeline(
            FunctionTransformer(extract_titles),
            OneHotEncoder(handle_unknown="ignore", sparse=False),
        ),
        title_feat,
    ),
    verbose_feature_names_out=False,
)

# ======= Model Pipeline =================

data_pipeline = make_union(pre_processing, featurize)

# ========================================


# Fit & Transform the selected columns, then rebuild the DataFrame
data_pipeline.fit(X_train)


# cols = featurize.get_feature_names_out()   # ohe does not provide get_feature_names_out()

X_train = pd.DataFrame(data_pipeline.transform(X_train), index=X_train.index)
X_test = pd.DataFrame(data_pipeline.transform(X_test), index=X_test.index)

# Rebuild the DataFrame
train_out = pd.concat([X_train, y_train], axis=1)
test_out = pd.concat([X_test, y_test], axis=1)

# Save the resulting datasets
joblib.dump(train_out, train_out_path)
joblib.dump(test_out, test_out_path)

# Save the pipeline
joblib.dump(featurize, pipeline_out_path)
