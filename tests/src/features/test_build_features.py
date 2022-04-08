# pylint: disable=E1120
"""Test src/data/make_dataset.py."""
import pytest
from src.features.build_features import main
import configparser


def test_main_no_args():
    """Test that the make_dataset.py script doesn't run without any
    arguments."""
    with pytest.raises(TypeError):
        main()


def test_main_with_args():
    """Test that the make_dataset.py script runs with the correct arguments."""

    config = configparser.ConfigParser()
    config.read("configs.ini")
    input_dir = config["datasets"]["raw_folder"]
    output_dir = config["datasets"]["processed_folder"]
    model_dir = config["datasets"]["model_folder"]

    """Test that the make_dataset.py script run with arguments."""
    with pytest.raises(FileNotFoundError):
        main(input_dir, output_dir, model_dir)
