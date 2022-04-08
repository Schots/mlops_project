# -*- coding: utf-8 -*-
"""This module is responsible for feature engineering such as normalization,
standardization, encoding, etc."""
import sys
import logging
import os
import argparse
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sklearn.pipeline import make_pipeline, make_union
from sklearn.compose import make_column_transformer, make_column_selector
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.preprocessing import FunctionTransformer

from custom_transformers import (
    identify_deck,
    fill_by_group,
    count_features,
    discretize_feature,
    boolean_feature,
    extract_titles,
)

import yaml

logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s | %(name)s | %(message)s"
)
logger = logging.getLogger(__name__)


def main(input_folder, output_folder, model_folder):

    # Open the configuration file. All the parameters are stored in the params.yaml file.
    # In this file the user can specify the parameters for the feature engineering, such as
    # the target, the preprocess steps, feature creation, feature selection, etc.
    try:
        with open("params.yaml", "r", encoding="utf-8") as file:
            # Load the entire file
            params = yaml.load(file, Loader=yaml.SafeLoader)
            # Find the target (y variable) in the file.
            target = params["dataset"]["target"]
            # Find the preprocess steps in the file.
            prepare = params["prepare"]

    except Exception as e:
        logger.error(f"{e}")
        sys.exit(1)

    # If doesn't exist, create the output data folder
    os.makedirs(output_folder, exist_ok=True)

    # Path to raw train.csv and test.csv data sets
    data_path = Path(f"{input_folder}/train.csv").resolve()

    # The resulting data of the featurization process will
    # be stored according to the following paths
    train_out_path = Path(f"{output_folder}/train.joblib").resolve()
    test_out_path = Path(f"{output_folder}/test.joblib").resolve()
    pipeline_out_path = Path(f"{model_folder}/features.joblib").resolve()

    # Load raw data and split in train and test
    data = pd.read_csv(data_path, index_col=[0])

    # Split the predictors and the target
    X, y = (
        data.drop(target, axis=1),
        data.pop(target),
    )

    # Split into train/test data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, **prepare, stratify=y
    )

    # ======= Data Pipeline =========

    data_pipeline = make_column_transformer(
        # Create the familysize feature
        (
            FunctionTransformer(count_features, kw_args={"offset": 1}),
            ["SibSp", "Parch"],
        ),
        # Create is_alone feature
        (FunctionTransformer(boolean_feature), ["SibSp", "Parch"]),
        # Create the title feature
        (
            make_pipeline(
                FunctionTransformer(extract_titles),
                OneHotEncoder(handle_unknown="ignore", sparse=False),
            ),
            ["Name"],
        ),
        # Create the deck feature
        (
            make_pipeline(
                FunctionTransformer(identify_deck),
                OneHotEncoder(handle_unknown="ignore", sparse=False),
            ),
            ["Cabin"],
        ),
        # Create the fare_band feature
        (
            make_pipeline(
                SimpleImputer(strategy="median"),
                FunctionTransformer(
                    discretize_feature,
                    kw_args=dict(
                        bins=[0, 8, 15, 32, 100, 600],
                        labels=[
                            "Very Low",
                            "Low",
                            "Medium",
                            "High",
                            "Very High",
                        ],
                    ),
                ),
                OrdinalEncoder(
                    categories=[
                        ["Very Low", "Low", "Medium", "High", "Very High"]
                    ]
                ),
            ),
            ["Fare"],
        ),
        # Create the age_band feature
        (
            make_pipeline(
                FunctionTransformer(
                    fill_by_group,
                    kw_args=dict(group_by="Pclass", fill_by="median"),
                ),
                FunctionTransformer(
                    discretize_feature,
                    kw_args=dict(
                        bins=[0, 14, 24, 64, 150],
                        labels=["Children", "Youth", "Adults", "Seniors"],
                    ),
                ),
                OrdinalEncoder(
                    categories=[["Children", "Youth", "Adults", "Seniors"]]
                ),
            ),
            ["Age", "Pclass"],
        ),
        (
            make_pipeline(
                SimpleImputer(strategy="most_frequent"),
                OneHotEncoder(handle_unknown="ignore", sparse=False),
            ),
            ["Embarked", "Sex", "Pclass"],
        ),
        ("passthrough", ["SibSp", "Parch"]),
    )

    # Fit & Transform the selected columns, then rebuild the DataFrame
    data_pipeline.fit(X_train)
    X_train = pd.DataFrame(
        data_pipeline.transform(X_train), index=X_train.index
    )
    X_test = pd.DataFrame(data_pipeline.transform(X_test), index=X_test.index)

    # Rebuild the DataFrame
    train_out = pd.concat([X_train, y_train], axis=1)
    test_out = pd.concat([X_test, y_test], axis=1)

    # Save the resulting datasets
    joblib.dump(train_out, train_out_path)
    joblib.dump(test_out, test_out_path)

    # Save the pipeline
    joblib.dump(data_pipeline, pipeline_out_path)

    sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Build features for the titanic dataset."
    )
    parser.add_argument(
        "-i",
        "--input_folder",
        type=str,
        default="data/raw",
        help="The folder where the raw data is stored.",
    )
    parser.add_argument(
        "-o",
        "--output_folder",
        type=str,
        default="data/processed",
        help="The folder where the processed data will be stored.",
    )
    parser.add_argument(
        "-m",
        "--model_folder",
        type=str,
        default="models",
        help="The folder where the models will be stored.",
    )
    args = parser.parse_args()
    main(**vars(args))
