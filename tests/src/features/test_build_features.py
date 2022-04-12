# pylint: disable=E1120, R0801
"""Test src/data/make_dataset.py."""
import os
from pathlib import Path
import configparser
import pytest
from src.features.build_features import main


# from tests.src.data.test_make_dataset import temp_folder, test_main_with_valid_DEV


def test_main_no_args_DEV():
    """Test that the make_dataset.py script doesn't run without any
    arguments."""
    with pytest.raises(TypeError):
        main()


def test_main_with_config_file_DEV(load_config):
    """Test that the make_dataset.py script runs with the correct arguments."""

    # Valid arguments
    input_folder = Path(load_config["datasets"]["raw_folder"]).resolve()
    output_folder = Path(load_config["datasets"]["processed_folder"]).resolve()
    models_folder = Path(load_config["datasets"]["models_folder"]).resolve()

    """Test that the make_dataset.py script run with arguments."""
    with pytest.raises(SystemExit):
        main(input_folder, output_folder, models_folder)


def test_main_with_valid_DEV(temp_folder):
    """Test that the make_dataset.py script runs with the correct arguments."""
    # Valid arguments

    input_folder = temp_folder / "raw"
    output_folder = temp_folder / "features"
    models_folder = temp_folder / "models"

    # print(input_folder, output_folder, models_folder)
    with pytest.raises(SystemExit):
        main(input_folder, output_folder, models_folder)
