"""Get data from kaggle."""
import argparse
import logging
import subprocess
import os
from pathlib import Path
from kaggle.api import KaggleApi


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def download_data(
    competition,
    train_data,
    test_data,
    output_dir,
    credentials=".kaggle/kaggle.json",
):

    """Downloading train and test data from Kaggle Titanic competition.

    Args:
        competition (str): name of competiton
        train_data (str): name of train dataset
        test_data (str): name of test dataset
    """
    credentials = Path.home().joinpath(credentials)

    api = KaggleApi()
    api.authenticate()

    logger.info("Downloading train data")
    subprocess.run(
        [
            "kaggle",
            "competitions",
            "download",
            competition,
            "-f",
            train_data,
            "--path",
            output_dir,
        ],
        check=True,
    )

    logger.info("Downloading test data")
    subprocess.run(
        [
            "kaggle",
            "competitions",
            "download",
            competition,
            "-f",
            test_data,
            "--path",
            output_dir,
        ],
        check=True,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--competition",
        dest="competition",
        required=True,
        help="Kaggle competition to download",
    )
    parser.add_argument(
        "-tr",
        "--train_data",
        dest="train_data",
        required=True,
        help="Train csv file",
    )
    parser.add_argument(
        "-te",
        "--test_data",
        dest="test_data",
        required=True,
        help="Test csv file",
    )
    parser.add_argument(
        "-o",
        "--out-dir",
        dest="output_dir",
        default=os.path.dirname(Path(__file__).resolve()),
        required=False,
        help="output directory",
    )
    args = parser.parse_args()

    download_data(
        args.competition,
        args.train_data,
        args.test_data,
        output_dir=args.output_dir,
    )
