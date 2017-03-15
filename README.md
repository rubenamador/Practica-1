# Sample Repository

This simple project is an example repo for Python projects for Verificación y Desarrollo de Software.

## Setup

1. Install Python
    1. (Windows) https://www.python.org/downloads/release/python-2713/
    2. (Mac) Installed yet
    3. (Linux) sudo apt-get install python2.7
2. Install environment
    1. Sublime Text (https://www.sublimetext.com/)
    2. PyCharm (https://www.jetbrains.com/pycharm/)
3. Install Pip (https://pypi.python.org/pypi/pip, https://pip.pypa.io/en/stable/installing/)
4. Install virtualenv (https://virtualenv.pypa.io/en/stable/installation/)
5. Instalar git
    1. https://git-scm.com/download/win
    2. `sudo apt-get install git`
    3. `git`
6. Clone this repo
7. Create a virtual env into the folder (i.e. ENV)
    1. `virtalenv ENV`
8. Activate the environment
    1. *NIX`source bin/activate`
    2. Windows `env\Scripts\activate`

## How to work with this repo

Open this repo with your IDE. Install requirements into your environment. You can use: 
1. `pip install -r requirements.txt`
2. `python setup.py install`
3. `make init`
  
## Execute tests
`make tests`

## Working with GIT
We need to create 2 different branches: `master` and `develop` (you can use [this](https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches))
- `master`: this will be the branch I want to evaluate.
- `develop`: use it to add all the code you develop

Everytime you want to pass code from develop to master you need to do a `pull request` and you need someone review your code. You can know more in [this](https://help.github.com/articles/about-pull-requests/) page.
