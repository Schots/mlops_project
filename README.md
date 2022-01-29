![](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white) 

![GitHub Contributors Image](https://contrib.rocks/image?repo=schots/mlops_project)

<div style="background-color:white;">
<h1 align="center"> <img width=300px src=img/logo.png> </h1>
</div>

## MLOps Project 
---
A project to learn how to build, deliver and maintain a Machine Learning service using the MLOps paradigm.

This study case aims to be testable and reproducible within the CI/CD methodology, using the best programming practices.

<br>

## How to contribute?
---
Following the steps below you will be able to contribute to this project by creating scripts, packages, doing changes, and more.

1. Download git

    Git is a version control tool, allowing many people can change files simultaneously, without the risk of lost changes or overwrite it.

    https://git-scm.com/downloads

2. Login or Create your github.com account

    https://github.com/

3. Create your personal access token

    The support for password authentication was removed, you need to use a personal access token to manage your repositories via terminal.

    [creating-a-personal-access-token-tutorial](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

4. Fork the repository
    
    Go to the project repository.

    https://github.com/Schots/mlops_project 
    
    and fork by clicking on the upper-left button.
    
    <img width=400px src=img/fork_button.png>

    this will make a [independent](https://docs.github.com/en/get-started/quickstart/fork-a-repo) copy of this repository in your GitHub, allowing you to make changes without affecting this repo, except via _**Pull Requests**_.

5. Clone the forked repository

    After forking, your copy will be listed on your repositories list.

    <img width=800px src=img/repositories.png >

    open the repository

    <img width=800px src=img/clone.png>
    
    copy the link provided by clicking on the button _Code_
    
    Open a bash terminal (if you are using Windows, make sure of using the git bash), navigate to the desired folder, and clone the forked repository to your machine.

    ```sh
    git clone https://github.com/<username>/mlops_project.git
    ```

6. Create your branch

    Create your own branch open a terminal inside the repository forked and type.
    
    ```sh
    git checkout -b my_branch
    ```

    then push your branch to your forked repository

    ```sh
    git push --set-upstream origin my_branch
    ```

7. Set up the environment

    Configure your local machine to work in this project. First create a virtual environment Python virtual environment for the MLOps project on your local machine.

    ```sh
    make create_environment
    ```

    Activate the environment and install dependencies

    ```sh
    workon mlops_project                # or 'conda activate mlops_project'
    make requirements
    ```

8. Creating a Pull Request
    
    a) Make your contributions! 
    
    :warning: Before commit and push, **don't forget** of adding the new **dependencies** to the right files. 

    :no_entry_sign: <span style="color:red">**In this project the requirements.txt and requirements-dev-in.txt will be generated, please don´t edit them.**</span>

    The project dependencies should be put into <span style="color:yellow">requirements.in</span> and <span style="color:yellow">requirements-dev.in</span> files (not the same dependency in both).
    
    - <span style="color:yellow">requirements.in</span> - you should put **scripts** and **modules** dependencies here.
    - <span style="color:yellow">requirements-dev.in</span> - you should put **development dependencies** like black, pylint and pytest here.

    <br>

    b) Commit and push your changes to sync your local repository with your own remote repository. Now, you'll be able to create a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

9. Example
    
    Create a branch called new_branch

    ```sh
    git checkout -b new_branch          # swith to the new_branch
    ```

    Create a Python script.py

    ```sh
    sudo nano script.py                 # to save type 'CRTL+X -> Yes or y -> Enter'
    ```

    Write the following program.

    _script.py_ :

    ```Python
    from passlib.context import CryptContext

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    hashed_password = pwd_context.hash("my_password")

    print(hashed_password)

    ```
    
    Make the script readable, writable and executable by giving permissions.

    ```sh
    sudo chmod +777 script.py           # add permission to the file
    ```

    As the script needs on ***passlib*** library, edit the <span style="color:yellow">requirements.in</span> file and include this dependency.

    _requirements.in_ :

    ```
    passlib
    ```
    
    Reinstall all dependencies of the project, which will also install the new dependencies that you have included in the requirements files.

    ```sh
    make requirements
    ```

    Test your script.

    ```sh
    python3 script.py
    ```

    If everything works fine you will see something like this output, a hashed password

    ```sh
    $2b$12$B.Xs4nChoe87oXAFM.QHNe7UkSWBWHh0ZuShzs/weKzKPoMKB.cbi
    ```

    Now commit and push your changes.

    ```sh
    git add script.py                   # add the file created
    git add requirements.in             # add the requirements changes
    git commit -m "First commit"        # commit the changes
    git push                            # push to the forked repository

    ```

    after this few steps, the following message will be displayed on your repository.

    <img src=img/pushed.png>

    now you can create your own [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)

<br>

## How to use?
---

If you are interested just in using this package, follow the steps below.

1. Clone the repository
    
    Open a terminal (if you are using Windows, make sure of using the git bash) navigate to the desired destination folder and clone the repository,
    
    ```sh
    git clone https://github.com/Schots/mlops_project.git
    ```

    The [Makefile](Makefile) on the root folder defines a set of functions needed to automate repetitive processes in this project. Type "make" in the terminal and see the available functions.

<br>

2. Create a virtual environment

    This step will create a python virtual environment for the MLOps project on your local machine

    ```sh
    make create_environment
    ```  
4. Generate kaggle api connection token

    Follow the steps to download a new authentication token onto your machine to complete the authentication:

    Make a directory named “.kaggle”.

    ```sh
    mkdir ~/.kaggle
    ```

    Click on your profile picture and click on Account from the drop-down menu. Scroll down to the API section and click on the ‘Create New API Token’ button to download a fresh token as a JSON file having a username and API key.

    Allocate the required permission for this file.
    
    ```sh
    chmod 600 ~/.kaggle/kaggle.json
    ```
    Add kaggle in requirements.in file.

5. Install requirements

    This step will install all requirements in your environment.

    ```sh
    make requirements
    ```

6. Download data

    To download the raw dataset, use the get_data

    ```sh
    make get_data
    ```
    type the dataset name when prompted. The zip file with data will be downloaded and unzipped under the _data/raw_ folder

<br>

## Project Organization
----

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
