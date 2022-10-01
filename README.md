![Python](https://shields.io/badge/Python-3.8%20%7C%203.9-blue)
[![GitHub release](https://img.shields.io/github/v/release/xofbd/unfair-coin-bayes.svg)](https://github.com/xofbd/unfair-coin-bayes/releases)
[![License: MIT](https://img.shields.io/github/license/xofbd/unfair-coin-bayes)](https://opensource.org/licenses/MIT)
![CI](https://github.com/xofbd/unfair-coin-bayes/workflows/CI/badge.svg?branch=master)
[![codecov](https://codecov.io/gh/xofbd/unfair-coin-bayes/branch/master/graph/badge.svg?token=Gal3jdSMI6)](https://codecov.io/gh/xofbd/unfair-coin-bayes)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/xofbd/unfair-coin-bayes.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/xofbd/unfair-coin-bayes/context:python)
[![Language grade: JavaScript](https://img.shields.io/lgtm/grade/javascript/g/xofbd/unfair-coin-bayes.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/xofbd/unfair-coin-bayes/context:javascript)

# Unfair Coin Bayesian Simulation
This repository creates a web app that simulates the evolving probability distribution of an unfair coin to come up heads using Bayes's theorem. The prior distribution is a Beta distribution with both shape parameters set to one, resulting in a uniform distribution. This repository is ready to deploy a web application using [Flask](https://flask.palletsprojects.com) and [Bokeh](https://bokeh.org) to Heroku. An example of the app can be seen at https://unfair-coin-bayes.herokuapp.com.

## Prerequisites
You will need either Python 3.8 or 3.9. All required Python packages can be found in the `requirements.txt` file. You will also need a Heroku account and have installed the Heroku CLI. For more information on the Heroku CLI, go to https://devcenter.heroku.com/articles/heroku-cli#download-and-install.

## Running the app locally using Flask
You may want to run the app using Flask locally before deploying it to Heroku, especially if you have made any changes to the code. To run locally:

1. clone the repository.
1. in the repository, run `make deploy-prod`.
1. open the link provided in the command line.

Alternatively, you can deploy using [Docker](https://www.docker.com/). You can run using `make docker-deploy` or
1. `docker build -t unfair-coin-bayes .`
1. `docker run --init --rm -d --publish 127.0.0.1:8000:8000 --env SECRET_KEY=$(bin/set-secret-key --) unfair-coin-bayes`

## Deploying to Heroku
Make sure your app is ready to be deployed to Heroku by running Flask locally. To deploy to Heroku:

1. clone the repository (if you haven't yet).
1. `heroku login` and enter your credentials.
1. `heroku create` or `heroku create app-name` where app-name is a custom app name.
1. `git push heroku master`.
1. `heroku open` or open the app online through your Heroku profile.

## License
This project is distributed under the MIT license. Please see `LICENSE` for more information.
