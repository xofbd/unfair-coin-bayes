SHELL := /bin/bash
ACTIVATE_VENV := source venv/bin/activate

ins := ${wildcard requirements/*.in}
reqs := ${ins:requirements/%.in=requirements/%.txt} requirements.txt
docker_image := unfair-coin-bayes
docker_container := app

.PHONY: all
all: clean deploy-prod

# Deployment
.PHONY: deploy-prod deploy-dev docker-image docker-run docker-stop

deploy-dev: .make.dev
	 ${ACTIVATE_VENV} && bin/run_app dev

deploy-prod: .make.prod
	 ${ACTIVATE_VENV} && bin/run_app prod

docker-image: requirements.txt
	docker build -t ${docker_image} .

docker-run: docker-image
	docker run --init --rm -d --publish 127.0.0.1:8000:8000 --name ${docker_container} ${docker_image}

docker-stop:
	docker container stop ${docker_container}

# Virtual Environments
.PHONY: venv-base venv-dev venv-prod

venv:
	python3 -m venv $@

venv-base: .make.base

.make.base: requirements/base.txt | venv
	${ACTIVATE_VENV} && pip install pip==20.3.0
	${ACTIVATE_VENV} && pip install -r $<
	touch $@

venv-prod: .make.prod

.make.prod: requirements/prod.txt | .make.base
	${ACTIVATE_VENV} && pip-sync $<
	rm -rf .make.dev
	touch $@

venv-dev: .make.dev

.make.dev: requirements/prod.txt requirements/dev.txt | .make.base
	${ACTIVATE_VENV} && pip-sync $^
	rm -rf .make.prod
	touch $@

# Requirements
.PHONY: requirements

requirements: ${reqs}

requirements/%.txt: requirements/%.in requirements/constraints.txt | .make.base
	${ACTIVATE_VENV} && pip-compile $<

requirements/dev.txt: requirements/prod.txt

requirements/base.txt:
 # Avoid circular reference caused by venv rule
	:

requirements.txt: requirements/prod.txt | .make.prod
	${ACTIVATE_VENV} && pip freeze > $@

# Utility
.PHONY: tests tests-unit tests-flake8 docker-rm clean

tests: test-unit test-lint

test-unit: .make.dev
	${ACTIVATE_VENV} && pytest -s --cov=app --cov-report=term --cov-report=xml

test-lint: .make.dev
	${ACTIVATE_VENV} && flake8 app tests

.PHONY: tox
tox: .make.dev
	$(ACTIVATE_VENV) && tox

clean:
	rm -rf venv .pytest_cache .coverage coverage.xml .make.* .tox
	find . | grep __pycache__ | xargs rm -rf
