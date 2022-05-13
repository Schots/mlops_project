import pytest
import yaml
from src.models.train_model import train

from sklearn.base import ClassifierMixin
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor


def test_ClassifierMixin():
    # a simple check to see if the ClassifierMixin is working
    assert isinstance(RandomForestClassifier(), ClassifierMixin)
    with pytest.raises(AssertionError):
        assert isinstance(RandomForestRegressor(), ClassifierMixin)


def test_train_model_raise_exception():
    with pytest.raises(ValueError):
        # change params.yaml at run time just to test the exception
        with open("params.yaml", "r", encoding="utf-8") as file:
            params = yaml.load(file, Loader=yaml.SafeLoader)
        params["train"]["clf"] = "RandomForestRegressor"
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
