# python-project-start
Set-up guide. Edit as appropriate.

## Download Python and Git
- [Python](https://www.python.org/downloads/)
- [Git](https://github.com/git-guides/install-git)

## Clone the GitHub repo
Navigate to a local folder and run:

    git clone git@github.com:mattwalmsley/python-project-starter.git

## Set-Up Python Virtual Environment
- [Using the command line](https://docs.python.org/3/using/cmdline)
- [venv](https://docs.python.org/3/library/venv.html)
- [Visual Studio Code Python Environments](https://code.visualstudio.com/docs/python/environments)

Create virtual environment with venv module (run this in python-project-starter directory)

<br>
Linux:

    python3 -m venv .venv

<br>
Windows/Mac:

    python -m venv .venv



<br>
Activate virtual environment:

    source .venv/bin/activate

<br>
Settings for <em>settings.json</em> in <em>.vscode</em>

    {
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python3",
    "python.envFile": "${workspaceFolder}/.venv"
    }

<br>
Install required packages for venv from file:

    pip install -r requirements.txt

<br>
Write/update required packages for venv to requirements file:

    pip freeze > requirements.txt
