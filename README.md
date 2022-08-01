# citi-hackathon-2022
Team C

## Notes on Python Set-Up

Create virtual environment with venv module

    python3 -m venv .venv

- [Using the command line](https://docs.python.org/3/using/cmdline)
- [venv](https://docs.python.org/3/library/venv.html)

<br>
Activate virtual environment:

    source .venv/bin/activate

<br>
Setting for settings.json in .vscode

    {
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python3",
    "python.envFile": "${workspaceFolder}/.venv"
    }

<br>
Install required packages for venv from file:

    pip install -r requirements.txt
