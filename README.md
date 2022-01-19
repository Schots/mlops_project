mlops_project
==============================
GITHUB

Passo a Passo para Clonar o repositório: (WIN)
     
     1º - Fazer o Download do GIT para sua máquina:
          (https://git-scm.com/downloads)

O Git é uma ferramenta de controle de versão. Ele possibilita que várias pessoas possam criar e alterar arquivos existentes de forma simultanea, sem que haja o risco das alterações sejam perdidas ou sobrescritas. O GIT funcionará pelo pronpt de comando.

    2º - Criar conta no GitHub:
         (https://github.com/)

Para clonar o repositório de trabalho no windows para sua máquina você deve acessar o prompt do Git (GIT BASH). Através dos comandos "cd" e "ls" você poderá escolher o diretório no qual irá trabalhar. O comando para clonar o projeto para o diretório que você está trabalhando é:
     
     3º - Clonar Repositório:
          git clone https://github.com/Schots/mlops_project.git

Push
     Abrir o Git-Bash (Prompt)
     1º - Acessar o diretório de trabalho por meio dos comandos "cd" e "ls"
     2º - Fazer os seguintes comandos: 
          
          git init | Cria um Reposítório normal na sua máquina
          git add . | Adiciona os arquivos que foram modificados ao repositório.
          git commit -m "<Nome do Commit>" | Os commits são as unidades de um cronograma de projeto Git.
          git remote add origin <URL DO REPOSITÓRIO REMOTO> | Acessa o repositório remoto no GIT
          git push origin <Nome do branch> | Envia os arquivos do diretório local para o diretório remoto.

          OBS: Caso você não saiba o nome do branch disponível você pode realizar o seguinte comando
          git show-ref
          Irá aparecer várias linhas, procure a linha que tem o seguinte caminho <refs/heads/main> 
          Neste caso o branch disponível tem o nome "main", mas poderia ter outro diferente.
     
     3º O prompt irá solicitar login e senha da conta do github pelo próprio prompt, é só inserir e o push será feito.

an end-to-end mlops project

Project Organization
------------

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
