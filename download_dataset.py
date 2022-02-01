import sys
import tempfile
import zipfile
import logging
import configparser
from pathlib import Path
import click

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


PROMPT_STRING = (
    "+----------------------------+\n|   Enter the dataset name  "
    " |\n+----------------------------+\n"
)


@click.command()
@click.option(
    "-d",
    "--dataset",
    "dataset",
    prompt=(PROMPT_STRING),
    help=(
        "Go to the Kaggle competition and copy the dataset name at the end of "
        '        command "kaggle competitions download"'
    ),
)
def download(dataset=None):
    """Function to download a kaggle competition dataset.

    Args:
        dataset (str): the dataset name.
    """

    # Load the raw data destination folder from the dataset config file
    config = configparser.ConfigParser()
    config.read("configs.ini")

    raw_data_folder = config["datasets"]["raw_folder"]
    raw_data_folder = Path(raw_data_folder).resolve()

    # try to import the kaggle api
    try:
        from kaggle.api import KaggleApi
    except OSError as error:
        logger.error(error)
        sys.exit()

    api = KaggleApi()
    api.authenticate()

    try:
        # Create a temporary folder to download dataset files in
        with tempfile.TemporaryDirectory() as temp_dir:
            # Download the dataset under the temporary folder
            api.competition_download_files(dataset, path=temp_dir)

            # Unzip the file download and transfer content to data/raw
            downloaded_file_path = f"{temp_dir}/{dataset}.zip"
            downloaded_file_path = Path(downloaded_file_path).resolve()

            with zipfile.ZipFile(downloaded_file_path, "r") as zip_ref:
                zip_ref.extractall(raw_data_folder)

            click.echo("Data downloaded!")

    except Exception as e:
        click.echo(e.reason)


if __name__ == "__main__":
    download()
