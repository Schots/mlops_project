# -*- coding: utf-8 -*-
import os
import logging
from pathlib import Path
import configparser
import click
from dotenv import find_dotenv, load_dotenv

ROOT_DIR = os.path.abspath(os.curdir)
print(ROOT_DIR)

config = configparser.ConfigParser()
config.read("configs.ini")

raw_data_folder = config["datasets"]["raw_folder"]
processed_data_folder = config["datasets"]["processed_folder"]


@click.command()
@click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def main(
    input_filepath=raw_data_folder, output_filepath=processed_data_folder
):
    """Runs data processing scripts to turn raw data from (../raw) into cleaned
    data ready to be analyzed (saved in ../processed)."""
    logger = logging.getLogger(__name__)
    logger.info("making final data set from raw data")


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
