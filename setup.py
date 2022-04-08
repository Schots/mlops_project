from setuptools import find_packages, setup

setup(
    name="src",
    packages=find_packages(exclude=["tests"]),
    version="0.1.0",
    description="An end-to-end mlops project",
    author="MLOps.br",
    license="MIT",
)
