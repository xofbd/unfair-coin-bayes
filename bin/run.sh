#!/bin/bash

if [[ -e venv ]]; then
    source venv/bin/activate
fi

export FLASK_APP=unfair_coin_bayes/app.py
export FLASK_ENV=development
export FLASK_DEBUG=1

HOST=${1:-127.0.0.1}
python -m flask run --host=$HOST
