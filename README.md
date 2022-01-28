![](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white) 

![GitHub Contributors Image](https://contrib.rocks/image?repo=schots/mlops_project)

<div style="background-color:white; height: 100%">
<h1 align="center"> <img width=300px src=img/logo.png> </h1>
</div>

## MLOps


The MLOps is the process of continuous integration and continuous delivery of Machine Learning artifacts as a software product, keeping it inside a loop of **Design**, **Model Development** and **Operations**.


<div align="center"><img width=400px src=img/mlopscicle.png></div>


<<<<<<< HEAD
In this paradigm, teams can easily collaborate in models, with clear tracking of the data throughout the process of cleaning, processing, and feature creation. Automating every repetitive process avoids human error and reduces the delivery time, ensuring the team keeps focusing on the **Business Problem**.
=======
In this paradigm teams can easily collaborate in models, with clear tracking of the data throughout the process of cleaning, processing, and feature creation. By automating every repetitive process avoiding human error in order to reduce the delivery time,to keep focusing on the **Business Problem.** 
>>>>>>> 1ad67d22b4e59631fbb9bf1c41229953e3304e44

Some benefits:

* Versioning data and code, making models to be auditable and reproducible.

* Automated tests and building ensuring quality functioning of artifacts and availability for the delivery pipelines.

* Makes it easier and faster the deployment of new models by using an automated cycle.

## The MLOps Project


The **MLOps project** is a path to learning how to implement a study case aiming to be testable and reproducible within the CI/CD methodology, using the best programming practices. 

The scope of this project is delimited as you can see in the image below.

We will select the best tool to implement every step, integrate them, and build a Machine Learning Orchestrator.  That said, in the end, new ML experiments will be easily made, and delivered as simples as typing a terminal command or clicking on a button!

<div align="center"><img width=500px src=img/mlopsscope.png></div>

<br>

## Prerequisites


For `mlops_project` to work correctly, first, you should install the [prerequisites](https://github.com/Schots/mlops_project/wiki#prerequisites) 

## Contributing


Have an idea of how to improve this project but don't know how to start, try to [contribute](https://github.com/Schots/mlops_project/wiki#how-to-contribute)

You can understand the project organization [here](https://github.com/Schots/mlops_project/wiki/The-Project-Template)


## How to use?


If you are interested just in using this package, follow the steps below.

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
    make get_data
    ```
    type the dataset name when prompted. The zip file with data will be downloaded and unzipped under the _data/raw_ folder

<br>


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
