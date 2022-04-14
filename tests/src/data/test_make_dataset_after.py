# pylint: disable=E1120, R0801
"""Test src/data/make_dataset_after.py."""
import pandas as pd
from pathlib import Path
import pytest


def test_data_is_pandas_dataframe_config_file_ENV(load_config):
    """Test that the data is a pandas dataframe."""

    raw_folder = Path(load_config["datasets"]["raw_folder"]).resolve()

    train_data = raw_folder.joinpath("train.csv")
    test_data = raw_folder.joinpath("test.csv")

    train_data = pd.read_csv(train_data)
    test_data = pd.read_csv(test_data)

    assert isinstance(train_data, pd.DataFrame)
    assert isinstance(test_data, pd.DataFrame)


def test_data_is_pandas_dataframe_temp_ENV(temp_folder):
    """Test that the data is a pandas dataframe."""

    raw_folder = temp_folder.joinpath("raw")

    train_data = raw_folder.joinpath("train.csv")
    test_data = raw_folder.joinpath("test.csv")

    train_data = pd.read_csv(train_data)
    test_data = pd.read_csv(test_data)

    assert isinstance(train_data, pd.DataFrame)
    assert isinstance(test_data, pd.DataFrame)
