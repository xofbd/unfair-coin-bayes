SHELL:=/bin/bash
ACTIVATE_VENV := source venv/bin/activate

.PHONY: all deploy-prod deploy-dev deploy-docker tests docker-rm clean

all: clean venv deploy-prod

venv: requirements.txt
	test -d venv || python3 -m venv venv
	${ACTIVATE_VENV} && pip install -r requirements.txt
	touch venv

# Deployment
deploy-dev: venv
	 ${ACTIVATE_VENV} && bin/run_app dev

deploy-prod: venv
	 ${ACTIVATE_VENV} && bin/run_app prod

deploy-docker: docker-rm
	docker build -t unfair_coin_bayes .
	docker run -d -p 5000:5000 --name coin_app unfair_coin_bayes

# Utility
tests: venv
	${ACTIVATE_VENV} && pytest -v tests

docker-rm:
	docker rm -f coin_app || echo "no container to remove"

clean:
	rm -rf venv
	rm -rf .pytest_cache
	find . | grep __pycache__ | xargs rm -rf
