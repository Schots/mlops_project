import sys
import pytest
from pytest_mock import mocker
import test_environment
from test_environment import main


def test_main_python_version():
    """Test the script by mocking global variable REQUIRED_PYTHON.

    Args:
        mocker (unknow): allows to replace parts of code or system for testing purposes
    """

    # test for invalid REQUIRED_PYTHON
    mocker.patch.object(test_environment, "REQUIRED_PYTHON", "python2")
    with pytest.raises(ValueError) as error:
        main()

    # test for invalid REQUIRED_PYTHON
    mocker.patch.object(test_environment, "REQUIRED_PYTHON", "python1")
    with pytest.raises(ValueError):
        main()

    # test for valid REQUIRED_PYTHON
    try:
        mocker.patch.object(test_environment, "REQUIRED_PYTHON", "python")
        # If the main() don't raises the ValueError, pytest.raises will raise an error!
        # which means that this REQUIRED_PYTHON="python" is valid
        with pytest.raises(ValueError):
            main()
    except:
        assert True

    # test for valid REQUIRED_PYTHON
    try:
        mocker.patch.object(test_environment, "REQUIRED_PYTHON", "python3")
        # If the main() don't raises the ValueError, pytest.raises will raise an error!
        # which means that this REQUIRED_PYTHON="python3" is valid
        with pytest.raises(ValueError):
            main()
    except:
        assert True


def test_main():
    """Test the script by mocking global variables REQUIRED_PYTHON and
    system_major.

    Args:
        mocker (unknow): allows to replace parts of code or system for testing purposes
    """
    # Assert that if installed python and REQUIRED PYTHON are the same
    # a TypeError doesn't will be raised
    try:
        mocker.patch.object(test_environment, "REQUIRED_PYTHON", "python")
        mocker.patch.object(test_environment, "system_major", 2)
        with pytest.raises(TypeError):
            main()
    except:
        assert True

    # Assert that if installed python and REQUIRED PYTHON are the same
    # a TypeError doesn't will be raised
    try:
        mocker.patch.object(test_environment, "REQUIRED_PYTHON", "python3")
        mocker.patch.object(test_environment, "system_major", 3)
        with pytest.raises(TypeError):
            main()
    except:
        assert True

    # Assert that a TypeError is raised if installed and REQUIRED_PYTHON are different
    mocker.patch.object(test_environment, "REQUIRED_PYTHON", "python3")
    mocker.patch.object(test_environment, "system_major", 2)
    with pytest.raises(TypeError):
        main()

    # Assert that a TypeError is raised if installed and REQUIRED_PYTHON are different
    mocker.patch.object(test_environment, "REQUIRED_PYTHON", "python")
    mocker.patch.object(test_environment, "system_major", 3)
    with pytest.raises(TypeError):
        main()
