# pylint: disable=E1120, R0801
"""Test src/data/make_dataset.py."""
import os
from pathlib import Path
import configparser
import pandas as pd
import pytest
from src.data.make_dataset import main


def test_main_no_args():
    """Test that the make_dataset.py script runs without any arguments."""
    with pytest.raises(TypeError):
        main()


def test_main_config_file_ENV(load_config):
    """Test that the make_dataset.py script runs with the correct arguments."""

    # Valid arguments
    competition_name = load_config["datasets"]["competition"]
    train_data = load_config["datasets"]["train"]
    test_data = load_config["datasets"]["test"]
    output_folder = Path(load_config["datasets"]["raw_folder"]).resolve()

    with pytest.raises(SystemExit):
        main(competition_name, train_data, test_data, output_folder)


def test_main_with_temp_ENV(temp_folder):
    """Test that the make_dataset.py script runs with the correct arguments."""
    # Valid arguments
    competition_name = "titanic"
    train_data = "train.csv"
    test_data = "test.csv"
    output_folder = temp_folder.joinpath("raw")

    # Create raw folder inside the temp_folder
    with pytest.raises(SystemExit):
        main(competition_name, train_data, test_data, output_folder)
