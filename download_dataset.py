import sys
import tempfile
import zipfile
import logging
import click
import configparser

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


try:
    from kaggle.api.kaggle_api_extended import KaggleApi, ApiException
except OSError as error:
    logger.error(error)
    sys.exit()

api = KaggleApi()
api.authenticate()


@click.command()
@click.option(
    "-d",
    "--dataset",
    prompt="+----------------------------+\n|   Enter the dataset name   |\n+----------------------------+\n",
    help='Go to the Kaggle competition and copy the dataset name at the end of \
        command "kaggle competitions download"',
)
def download(dataset):

    # Load the raw data destination folder from the dataset config file
    config = configparser.ConfigParser()
    config.read("configs.ini")

    raw_data_folder = config["datasets"]["raw_folder"]

    """Function to download a kaggle competition dataset.

    Args:
        dataset (str): the dataset name.
    """
    # Test the system type (Windows, Linux)
    # save in the temporary system folder
    try:
        # Create a temporary folder to download dataset files in
        with tempfile.TemporaryDirectory() as temp_dir:
            # Download the dataset under the temporary folder
            api.competition_download_files(dataset, path=temp_dir)
            # Unzip the file download and transfer content to data/raw
            with zipfile.ZipFile(f"{temp_dir}/{dataset}.zip", "r") as zip_ref:
                zip_ref.extractall(raw_data_folder)

    except ApiException as e:
        click.echo(e.reason)


if __name__ == "__main__":
    download()
