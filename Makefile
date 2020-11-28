SHELL:=/bin/bash

.PHONY: all deploy-prod deploy-dev deploy-docker docker-rm clean

all: clean venv deploy-prod

venv: requirements.txt
	test -d venv || python3 -m venv venv
	source venv/bin/activate && pip install -r requirements.txt
	touch venv

deploy-dev: venv
	 source venv/bin/activate && bin/run_app dev

deploy-prod: venv
	 source venv/bin/activate && bin/run_app prod

deploy-docker: docker-rm
	docker build -t unfair_coin_bayes .
	docker run -d -p 5000:5000 --name coin_app unfair_coin_bayes

docker-rm:
	docker rm -f coin_app || echo "no container to remove"

clean:
	rm -rf venv
	find . | grep __pycache__ | xargs rm -rf
