mlops_project
==============================
GITHUB

Passo a passo para clonar o repositório no GITHUB: (WINDOWS E LINUX)
     
     1º - Fazer o Download do GIT para sua máquina:
          (https://git-scm.com/downloads)

O Git é uma ferramenta de controle de versão. Ele possibilita que várias pessoas possam criar e alterar arquivos existentes de forma simultanea sem que haja o risco das alterações sejam perdidas ou sobrescritas. 

    2º - Criar conta no GitHub:
         (https://github.com/)

Para clonar o repositório remoto de trabalho no Windows para sua máquina você deve acessar o prompt do GIT em seu computador (barra de procura >> GIT BASH), caso você esteja utilizando LINUX os comandos serão feitos via SHELL. Através dos comandos "cd" e "ls" você poderá escolher o diretório do seu computador onde estão os arquivos do projeto nos quais você irá trabalhar. O comando para clonar o projeto para o diretório em que você está trabalhando é:
     
     3º - Clonar Repositório:
          git clone https://github.com/Schots/mlops_project.git


PUSH 
     1º - Abra o Git-Bash (Prompt - Windows) em seu computador;
     1º - Acesse o diretório de trabalho do seu computador onde estão os arquivos do projeto por meio dos comandos "cd" e "ls";
     2º - Realizar os seguintes comandos: 
          
          git init | O comando git init cria um novo repositório do Git. Ele pode ser usado para converter um projeto existente e não versionado em um repositório do Git ou inicializar um novo repositório vazio. 
          
          git add . | O comando git add adiciona todas as alterações no diretório ativo à área de staging. Ele diz ao Git que você quer incluir atualizações a um arquivo específico no próximo commit. No entanto, git add não tem efeito real e significativo no repositório — as alterações não são gravadas mesmo até você executar git commit .

          git commit -m "<Nome do Commit>" | Podem ser considerados instantâneos ou marcos ao longo do cronograma de um projeto Git. São criados com o comando git commit para capturar o estado de um projeto naquele momento.
          
          git push origin <Nome da branch> | Envia os arquivos do diretório local para o diretório remoto.

          OBS: Caso você não saiba o nome do branch disponível você pode realizar o seguinte comando
          
          git show-ref | Irá aparecer várias linhas, procure a linha que tem o seguinte caminho <refs/heads/main> 
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
