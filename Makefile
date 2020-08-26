SHELL:=/bin/bash

.PHONY: all deploy docker-deploy docker-rm remove_venv

all: venv deploy

venv: requirements.txt
	test -d venv || python3 -m venv venv
	source venv/bin/activate && pip install -r requirements.txt
	touch venv

deploy: venv
	 bin/run.sh

docker-deploy:
	docker build -t unfair_coin_bayes .
	docker run -d -p 5000:5000 --name flask_app unfair_coin_bayes

docker-rm:
	docker rm -f flask_app

remove_venv:
	rm -rf venv
