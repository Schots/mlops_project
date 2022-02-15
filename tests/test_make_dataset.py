"""Test make_dataset.py."""
import configparser
import yaml


def test_download_data():
    """test if the output parameters of the make_dataset module are correct."""
    config = configparser.ConfigParser()
    config.read("configs.ini")
    output_dir = config["datasets"]["raw_folder"]

    with open("dvc.yaml", "r") as file:
        stages_dvc = yaml.safe_load(file)
    output_dvc = stages_dvc["stages"]["data"]["outs"][0]

    assert output_dir == output_dvc
