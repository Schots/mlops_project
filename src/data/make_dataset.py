"""Get data from kaggle."""
import configparser
import logging
import subprocess
from kaggle.api import KaggleApi


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def download_data():

    """Downloading train and test data from Kaggle Titanic competition."""
    config = configparser.ConfigParser()
    config.read("../../configs.ini")
    competition_name = config["datasets"]["competition"]
    train_data = config["datasets"]["train"]
    test_data = config["datasets"]["test"]
    output_dir = config["datasets"]["raw_folder"]

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
            f"{output_dir}",
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
            f"{output_dir}",
        ],
        check=True,
    )


if __name__ == "__main__":

    download_data()
