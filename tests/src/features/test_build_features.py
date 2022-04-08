# pylint: disable=E1120
"""Test src/data/make_dataset.py."""
import pytest
from src.features.build_features import main


def test_main_no_args():
    """Test that the make_dataset.py script doesn't run without any
    arguments."""
    with pytest.raises(TypeError):
        main()


def test_main_with_invalid_args():
    """Test that the make_dataset.py script run with arguments."""
    with pytest.raises(FileNotFoundError):
        main(1, "a", [])
