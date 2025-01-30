# site-planner-api

## Running app locally

Needs to run in a virtual environment with its dependencies.

- `python3 -m venv venv`: creates the initial virtual environment.
- `source venv/bin/activate`: activate the virtual environment, should see (env in command line).
- `pip install flask`: installs flask.
- `pip freeze > requirements.txt`: makes a requirements file.
- `deactivate`: stops the virtual environment running.

## Requirements file

`pip install -r requirements.txt`:  Install packages from requirements files in a virtual environment

Any time a new dependency is added the requirements file needs to be updated.

- `pip freeze > requirements.txt`: makes a requirements file  (TODO: consider a precommit hook)

## Helpful commands

- `pip list`: list packages

## Run locally

- `python index.py`


## Run PSQL Locally

TODO: Dockerise it

- `psql postgres://johnjameshodgins@localhost:5432/johnjameshodgins`

