#!/bin/sh

# Enables hot reloading
export FLASK_DEBUG=1

export FLASK_APP=./api/index.py

# Activates virtual environment; finds and executes dependencies
source $(pipenv --venv)/bin/activate

# Runs flask listening on all interfaces
flask run -h 0.0.0.0