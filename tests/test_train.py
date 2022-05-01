import pytest
import yaml
from src.models.train_model import train


def test_train_model_raise_exception():
    with pytest.raises(ValueError):
        # change params.yaml at run time just to test the exception
        with open("params.yaml", "r", encoding="utf-8") as file:
            params = yaml.load(file, Loader=yaml.SafeLoader)
        params["train"]["clf"] = "WrongClassifier"
        input_folder = "data/processed"
        model_folder = "models"
        train(input_folder, model_folder, params)


def test_train_model__wrong_params_raise_exception():
    with pytest.raises(ValueError):
        # change params.yaml at run time just to test the exception
        with open("params.yaml", "r", encoding="utf-8") as file:
            params = yaml.load(file, Loader=yaml.SafeLoader)
        params["train"]["clf_params"]["Invalid_Arg"] = "Invalid_Value"
        input_folder = "data/processed"
        model_folder = "models"
        train(input_folder, model_folder, params)
