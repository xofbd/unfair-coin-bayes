SHELL := /bin/bash
ACTIVATE_VENV := source venv/bin/activate
REQS := ${wildcard requirements/*.txt} requirements.txt
OUTPUTS := .base .prod .dev

.PHONY: all
all: clean deploy-prod

# Deployment
.PHONY: deploy-prod deploy-dev deploy-docker

deploy-dev: .dev
	 ${ACTIVATE_VENV} && bin/run_app dev

deploy-prod: .prod
	 ${ACTIVATE_VENV} && bin/run_app prod

deploy-docker: docker-rm
	docker build -t unfair_coin_bayes .
	docker run -d -p 5000:5000 --name coin_app unfair_coin_bayes

# Virtual Environments
.PHONY: base dev prod

venv:
	python3 -m venv $@

base: .base

.base: requirements/base.txt venv
	${ACTIVATE_VENV} && pip install -r $<
	touch $@	

prod: .prod

.prod: requirements/prod.txt .base venv
	${ACTIVATE_VENV} && pip-sync $<
	rm -rf .dev
	touch $@

dev: .dev

.dev: requirements/dev.txt requirements/prod.txt venv
	${ACTIVATE_VENV} && pip-sync ${filter-out venv, $^}
	rm -rf .prod
	touch $@

# Requirements
.PHONY: requirements

requirements: ${REQS}

requirements/%.txt: requirements/%.in .base
	${ACTIVATE_VENV} && pip-compile $<

requirements/dev.txt: requirements/prod.txt

requirements/base.txt:
	: # Avoid circular reference caused by venv rule

requirements.txt: .prod
	${ACTIVATE_VENV} && pip freeze > $@

# Utility
.PHONY: tests docker-rm clean

tests: .dev
	${ACTIVATE_VENV} && pytest -s tests

docker-rm:
	-docker rm -f coin_app

clean:
	rm -rf venv .pytest_cache
	rm -f ${OUTPUTS}
	find . | grep __pycache__ | xargs rm -rf
