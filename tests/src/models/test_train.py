# pylint: disable=E1120, R0801
"""Test src/data/make_dataset.py."""
import os
from pathlib import Path
import configparser
import pytest

from src.models.train_model import main


def test_main_no_args():
    """Test that the make_dataset.py script doesn't run without any
    arguments."""
    with pytest.raises(TypeError):
        main()


def test_main_with_config_file_ENV(load_config):
    """Test that the make_dataset.py script runs with the correct arguments."""

    # Valid arguments
    input_folder = Path(load_config["datasets"]["processed_folder"]).resolve()
    models_folder = Path(load_config["datasets"]["models_folder"]).resolve()

    """Test that the make_dataset.py script run with arguments."""
    with pytest.raises(SystemExit):
        main(input_folder, models_folder)


def test_main_with_temp_ENV(temp_folder):
    """Test that the make_dataset.py script runs with the correct arguments."""
    # Valid arguments

    input_folder = temp_folder / "processed"
    models_folder = temp_folder / "models"

    with pytest.raises(SystemExit):
        main(input_folder, models_folder)
