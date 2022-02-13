import os
from src.data.make_dataset import download_data


def test_download_data():
    """Test that download_data() works."""
    download_data()
    assert os.path.exists(os.path.join(os.getcwd(), "data/raw", "train.csv"))
    assert os.path.exists(os.path.join(os.getcwd(), "data/raw", "test.csv"))
