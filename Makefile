SHELL := /bin/bash
ACTIVATE_VENV := source venv/bin/activate

ins := ${wildcard requirements/*.in}
reqs := ${ins:requirements/%.in=requirements/%.txt} requirements.txt
docker_image := unfair-coin-bayes
docker_container := app

.PHONY: all
all: clean deploy-prod

# Deployment
.PHONY: deploy-dev
deploy-dev: .make.dev
	 ${ACTIVATE_VENV} && bin/run_app dev

.PHONY: deploy-prod
deploy-prod: .make.prod
	 ${ACTIVATE_VENV} && bin/run_app prod

.PHONY: docker-image
docker-image: requirements.txt
	docker build -t ${docker_image} .

.PHONY: docker-run
docker-run: docker-image
	docker run --init --rm -d --publish 127.0.0.1:8000:8000 --name ${docker_container} ${docker_image}

.PHONY: docker-stop
docker-stop:
	docker container stop ${docker_container}

# Virtual Environments
venv:
	python3 -m venv $@

.PHONY: venv-base
venv-base: .make.base

.make.base: requirements/base.txt | venv
	${ACTIVATE_VENV} && pip install pip==20.3.0
	${ACTIVATE_VENV} && pip install -r $<
	touch $@

.PHONY: venv-prod
venv-prod: .make.prod

.make.prod: requirements/prod.txt | .make.base
	${ACTIVATE_VENV} && pip-sync $<
	rm -rf .make.dev
	touch $@

.PHONY: venv-dev
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
.PHONY: tests
tests: test-unit test-lint test-docker

.PHONY: test-unit
test-unit: .make.dev
	${ACTIVATE_VENV} && pytest -s --cov=app --cov-report=term --cov-report=xml

.PHONY: test-lint
test-lint: .make.dev
	${ACTIVATE_VENV} && flake8 app tests

.PHONY: test-docker
test-docker:
	tests/test-docker

.PHONY: tox
tox: .make.dev
	$(ACTIVATE_VENV) && tox

.PHONY: clean
clean:
	rm -rf venv .pytest_cache .coverage coverage.xml .make.* .tox
	find . | grep __pycache__ | xargs rm -rf
