"""Module to test environment."""
import sys
import configparser


def main():
    """This function will test if the Python version installed matches the
    required.

    Raises:
        ValueError: When neither Python2 nor Python3 was settled as required
        TypeError: When the required and the installed Python interpreter aren't the same.
    """

    config = configparser.ConfigParser()
    config.read("configs.ini")

    required_python = config["python_version"]["required_python"]

    if required_python == "python":
        required_major = 2
    elif required_python == "python3":
        required_major = 3
    else:
        raise ValueError(f"Unrecognized python interpreter: {required_python}")

    system_major = sys.version_info.major

    if system_major != required_major:
        raise TypeError(
            f"This project requires Python {required_major}. Found: Python"
            f" {sys.version}"
        )

    print(">>> Development environment passes all tests!")


if __name__ == "__main__":
    main()
