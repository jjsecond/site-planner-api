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

Need to be running the virtual environment if not already:

- `source venv/bin/activate`
- `python app.py`


## Run PSQL Locally

TODO: Dockerise it

- `psql postgres://johnjameshodgins@localhost:5432/johnjameshodgins`


## Additional Documentation

### DB Design

The DB is a postgres database.

The design can be found at: [Site DB Design](docs/siteDBDesign.pdf)
