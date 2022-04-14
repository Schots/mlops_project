import os
import pandas as pd
import configparser
from pathlib import Path
import joblib
import pytest


def test_features_is_pandas_dataframe_config_file(load_config):
    """Test that the data is a pandas dataframe."""

    # Features folder
    processed_folder = Path(
        load_config["datasets"]["processed_folder"]
    ).resolve()

    # Path to the data
    train_features = processed_folder.joinpath("train.joblib")
    test_features = processed_folder.joinpath("test.joblib")

    # Load the data
    train_df = joblib.load(train_features)
    test_df = joblib.load(train_features)

    # Check if the data is a pandas dataframe
    assert isinstance(train_df, pd.DataFrame)
    assert isinstance(test_df, pd.DataFrame)


def test_features_is_pandas_dataframe_temp_ENV(temp_folder):
    """Test that the data is a pandas dataframe."""

    # Features folder
    processed_folder = temp_folder.joinpath("processed")
    # Path to the data
    train_features = processed_folder.joinpath("train.joblib")
    test_features = processed_folder.joinpath("test.joblib")

    # Load the data
    train_df = joblib.load(train_features)
    test_df = joblib.load(train_features)

    # Check if the data is a pandas dataframe
    assert isinstance(train_df, pd.DataFrame)
    assert isinstance(test_df, pd.DataFrame)
