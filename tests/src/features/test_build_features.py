# pylint: disable=E1120
"""Test src/data/make_dataset.py."""
import pytest
from src.features.build_features import main


def test_main_no_args():
    """Test that the make_dataset.py script runs without any arguments."""
    with pytest.raises(TypeError):
        main()


def test_main_with_args():
    """Test that the make_dataset.py script doesn't runs with arguments."""
    with pytest.raises(TypeError):
        main(1, 1, 1)
