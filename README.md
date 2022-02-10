[![](https://github.com/Schots/mlops_project/actions/workflows/forked.yml/badge.svg)](https://github.com/Schots/mlops_project/actions/workflows/forked.yml)
![](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)
![Dependabot](https://img.shields.io/badge/dependabot-025E8C?style=for-the-badge&logo=dependabot&logoColor=white)

![GitHub Contributors Image](https://contrib.rocks/image?repo=schots/mlops_project)

<div style="background-color:white; height: 100%">
<h1 align="center"> <img width=300px src=img/logo.png> </h1>
</div>

## MLOps


The MLOps is the process of continuous integration and continuous delivery of Machine Learning artifacts as a software product, keeping it inside a loop of **Design**, **Model Development** and **Operations**.


<div align="center"><img width=400px src=img/mlopscicle.png></div>


In this paradigm, teams can easily collaborate in models, with clear tracking of the data throughout the process of cleaning, processing, and feature creation. Automating every repetitive process avoids human error and reduces the delivery time, ensuring the team keeps focusing on the **Business Problem**.

Some benefits:

* Versioning data and code, making models auditable and reproducible.

* Automated tests and building ensuring quality functioning of artifacts and availability for the delivery pipelines.

* Makes it easier and faster the deployment of new models by using an automated cycle.

## The MLOps Project


The **MLOps project** is a path to learning how to implement a study case aiming to be testable and reproducible within the CI/CD methodology, using the best programming practices. 

The scope of this project is delimited as you can see in the image below.

We will select the best tool to implement every step, integrate them, and build a Machine Learning Orchestrator.  That said, in the end, new ML experiments will be easily made, and delivered as simple as typing a terminal command or clicking on a button!

<div align="center"><img width=500px src=img/mlopsscope.png></div>

<br>

This project is structured following the [cookiecutter template](https://drivendata.github.io/cookiecutter-data-science/) and uses tools such as pre-commit to make it easier for other people to contribute.

You can understand the project organization [here](https://github.com/Schots/mlops_project/wiki/1.-The-Project-Template). 


## Prerequisites

For `mlops_project` to work correctly, first, you should install the [prerequisites](https://github.com/Schots/mlops_project/wiki#1-prerequisites) 

## Contributing

If you are interested in contributing to this project but you are a begginer on Github or never contributed to a project before, consider following [this tutorial](https://github.com/Schots/mlops_project/wiki/2.-Getting-started)

If you are familiar with open source projects and have an idea of how to improve this project follow the links below

* [How to commit and contribute to the MLOps Project](https://github.com/Schots/mlops_project/wiki/3.-How-to-commit-and-contribute-to-the-MLOps-Project)

* [Contribution Example](https://github.com/Schots/mlops_project/wiki/4.-Contribution-Example)

* [How to write good commit messages](https://github.com/Schots/mlops_project/wiki/5.-Writing-Meaningful-Commit-Messages)


## How to use?

If you are just interested in using this package, follow the steps below:

1. Clone the repository
    
    Open a terminal (if you are using Windows, make sure of using the git bash) navigate to the desired destination folder and clone the repository,
    
    ```sh
    git clone https://github.com/Schots/mlops_project.git
    ```

    The [Makefile](Makefile) on the root folder defines a set of functions needed to automate repetitive processes in this project. Type "make" in the terminal and see the available functions.

<br>

2. Create an environment & Install requirements

    Create a Python virtual environment for the MLOps project on your local machine. Use any tool you desire. Activate the environment and install the requirements using `make`:

    ```sh
    make requirements
    ```

3. Download data

    To download the raw dataset, use the get_data

    ```sh
    make data
    ```
    type the dataset name when prompted. The zip file with data will be downloaded and unzipped under the _data/raw_ folder

<br>

## Contributors

This project is the result of the collaboration of many people. 
Feel free to contact us on LinkedIn

<img src="https://contrib.rocks/image?repo=Schots/Data-Pills" width="50"> [Maykon Schots](https://www.linkedin.com/in/maykon-schots/)

<img src="https://contrib.rocks/image?repo=maikereis/introduction_to_statistics" width="50"> [Maike Reis](https://www.linkedin.com/in/maikereis/)

<img src="https://contrib.rocks/image?repo=stdogpkg/cukuramoto" width="50"> [Bruno Messias](https://www.linkedin.com/in/bruno-messias-510553193/)

<img src="https://contrib.rocks/image?repo=ElisaRMA/Coursera-Data-Science-Specialization" width="50"> [Elisa Ribeiro](https://www.linkedin.com/in/elisarma/)


<img src="https://contrib.rocks/image?repo=bobcastaldeli/Resume" width="50"> [Roberto Castaldelli](https://github.com/bobcastaldeli)

*Jaime Cirilo

<img src="https://contrib.rocks/image?repo=gusbruschi13/gusbruschi13" width="50"> [Gustavo Bruschi](https://www.linkedin.com/in/gustavo-bruschi/)

<img src="https://contrib.rocks/image?repo=leonsolon/meli-data-challente-2021" width="50"> [Leon Silva](https://www.linkedin.com/in/leonsolon/)

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
