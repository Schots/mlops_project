"""Get data from kaggle."""
import sys
import configparser
import argparse
import logging
import subprocess
from pathlib import Path
from kaggle.api import KaggleApi


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(name)s | %(message)s"
)
logger = logging.getLogger()


def main(competition_name, train_data, test_data, output_folder):
    """Get data from Kaggle.

    Args:
        competition_name (str): the name of the Kaggle competition
        train_data (str): the filename of the train dataset
        test_data (str): the filename of the test dataset
        output_folder (pathlib): the folder where the downloaded data will be saved
    """

    api = KaggleApi()
    api.authenticate()

    logger.info("Downloading train data")
    subprocess.run(
        [
            "kaggle",
            "competitions",
            "download",
            f"{competition_name}",
            "-f",
            f"{train_data}",
            "--path",
            f"{output_folder}",
        ],
        check=True,
    )

    logger.info("Downloading test data")
    subprocess.run(
        [
            "kaggle",
            "competitions",
            "download",
            f"{competition_name}",
            "-f",
            f"{test_data}",
            "--path",
            f"{output_folder}",
        ],
        check=True,
    )

    sys.exit(0)


if __name__ == "__main__":

    config = configparser.ConfigParser()
    config.read("configs.ini")
    competition = config["datasets"]["competition"]
    train_data = config["datasets"]["train"]
    test_data = config["datasets"]["test"]
    raw_folder = Path(config["datasets"]["raw_folder"]).resolve()

    parser = argparse.ArgumentParser(description="Download datasets.")
    parser.add_argument(
        "-c",
        "--competition_name",
        type=str,
        default=competition,
        help="Competition name.",
    )
    parser.add_argument(
        "--train_data",
        type=str,
        default=train_data,
        help="Train filename.",
    )
    parser.add_argument(
        "--test_data",
        type=str,
        default=test_data,
        help="Test filename",
    )
    parser.add_argument(
        "-o",
        "--output_folder",
        type=str,
        default=raw_folder,
        help="Output folder path.",
    )

    args = parser.parse_args()

    main(**vars(args))
