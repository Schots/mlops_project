import yaml
import pytest

PARAMS_FILE = "params.yaml"


def test_params_exist():
    """Test if the params.yaml file exists and is in the right format."""

    with open(PARAMS_FILE, "r", encoding="utf-8") as file:
        # Load the entire file
        params = yaml.load(file, Loader=yaml.SafeLoader)

    # Assert that the file isn't empty
    assert params is not None
    assert isinstance(params, dict)
