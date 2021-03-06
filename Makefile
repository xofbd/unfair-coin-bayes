SHELL := /bin/bash
ACTIVATE_VENV := source venv/bin/activate
DOCKER_IMAGE := unfair_coin_bayes
DOCKER_CONTAINER := coin_app

ins := ${wildcard requirements/*.in}
reqs := ${ins:requirements/%.in=requirements/%.txt} requirements.txt
outputs := .base .dev .prod

.PHONY: all
all: clean deploy-prod

# Deployment
.PHONY: deploy-prod deploy-dev deploy-docker

deploy-dev: .dev
	 ${ACTIVATE_VENV} && bin/run_app dev

deploy-prod: .prod
	 ${ACTIVATE_VENV} && bin/run_app prod

deploy-docker: docker-rm
	docker build -t ${DOCKER_IMAGE} .
	docker run -d -p 5000:5000 --name ${DOCKER_CONTAINER} ${DOCKER_IMAGE}

# Virtual Environments
.PHONY: base dev prod

venv:
	python3 -m venv $@

base: .base

.base: requirements/base.txt | venv
	${ACTIVATE_VENV} && pip install -r $<
	touch $@

prod: .prod

.prod: requirements/prod.txt | .base
	${ACTIVATE_VENV} && pip-sync $<
	rm -rf .dev
	touch $@

dev: .dev

.dev: requirements/prod.txt requirements/dev.txt | .base
	${ACTIVATE_VENV} && pip-sync $^
	rm -rf .prod
	touch $@

# Requirements
.PHONY: requirements

requirements: ${reqs}

requirements/%.txt: requirements/%.in requirements/constraints.txt | .base
	${ACTIVATE_VENV} && pip-compile $<

requirements/dev.txt: requirements/prod.txt

requirements/base.txt:
 # Avoid circular reference caused by venv rule
	:

requirements.txt: requirements/prod.txt | .prod
	${ACTIVATE_VENV} && pip freeze > $@

# Utility
.PHONY: tests tests-unit tests-flake8 docker-rm clean

tests: tests-unit tests-flake8

tests-unit: .dev
	-${ACTIVATE_VENV} && pytest -s tests

tests-flake8: .dev
	-${ACTIVATE_VENV} && flake8 unfair_coin_bayes tests

docker-rm:
	-docker rm -f ${DOCKER_CONTAINER}

clean:
	rm -rf venv .pytest_cache
	rm -f ${outputs}
	find . | grep __pycache__ | xargs rm -rf
