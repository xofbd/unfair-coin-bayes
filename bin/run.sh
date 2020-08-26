#!/bin/bash

source venv/bin/activate
export FLASK_APP="flask_app/app.py"
HOST=${1:-127.0.0.1}
python -m flask run --host=$HOST
