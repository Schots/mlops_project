# pylint: disable=E1121
"""Test src/data/make_dataset.py."""
import pytest
from src.data.make_dataset import main


def test_main_no_args():
    """Test that the make_dataset.py script runs without any arguments."""
    with pytest.raises(SystemExit):
        main()


def test_main_with_args():
    """Test that the make_dataset.py script run with arguments."""
    with pytest.raises(TypeError):
        main(1)
