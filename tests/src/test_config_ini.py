import configparser
import pytest

CONFIG_FILE = "configs.ini"


def test_config_file():
    """Test if the config.ini file exists and is in the right format."""

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    assert config is not None
    assert isinstance(config, configparser.ConfigParser)

    assert config.has_option(section="datasets", option="competition")
    assert config.has_option(section="datasets", option="train")
    assert config.has_option(section="datasets", option="test")
    assert config.has_option(section="datasets", option="raw_folder")
    assert config.has_option(section="datasets", option="processed_folder")
    assert config.has_option(section="datasets", option="models_folder")
    assert config.has_option(section="datasets", option="reports_folder")
    assert config.has_option(
        section="python_version", option="required_python"
    )
