"""The fixtures defined in this file will be available to every test."""
import configparser
import pytest

CONFIG_FILE_PATH = "configs.ini"


@pytest.fixture(scope="session", autouse=True)
def temp_folder(tmp_path_factory):
    """This fixture creates a temporary folder, then tests can share the same
    temporary folder."""
    tempfolder = tmp_path_factory.mktemp("data")

    raw_temp = tempfolder / "raw"
    raw_temp.mkdir()

    processed_temp = tempfolder / "processed"
    processed_temp.mkdir()

    models_temp = tempfolder / "models"
    models_temp.mkdir()

    return tempfolder


@pytest.fixture(scope="session", autouse=True)
def load_config():
    """Load a config file defined in the root of the project."""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_PATH)
    return config
