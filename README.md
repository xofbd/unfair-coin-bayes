![Python](https://shields.io/badge/Python-3.8%20%7C%203.9-blue)
[![GitHub release](https://img.shields.io/github/v/release/xofbd/unfair-coin-bayes.svg)](https://github.com/xofbd/unfair-coin-bayes/releases)
[![License: MIT](https://img.shields.io/github/license/xofbd/unfair-coin-bayes)](https://opensource.org/licenses/MIT)
![CI](https://github.com/xofbd/unfair-coin-bayes/workflows/CI/badge.svg?branch=master)
[![codecov](https://codecov.io/gh/xofbd/unfair-coin-bayes/branch/master/graph/badge.svg?token=Gal3jdSMI6)](https://codecov.io/gh/xofbd/unfair-coin-bayes)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/xofbd/unfair-coin-bayes.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/xofbd/unfair-coin-bayes/context:python)
[![Language grade: JavaScript](https://img.shields.io/lgtm/grade/javascript/g/xofbd/unfair-coin-bayes.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/xofbd/unfair-coin-bayes/context:javascript)

# Unfair Coin Bayesian Simulation
This repository creates a web app that simulates the evolving probability distribution of an unfair coin to come up heads using Bayes's theorem. The prior distribution is a Beta distribution with both shape parameters set to one, resulting in a uniform distribution. This repository is ready to deploy a web application using [Flask](https://flask.palletsprojects.com) and [Bokeh](https://bokeh.org) to services such as [Render](https://render.com/). An example of the app can be seen at [here](https://unfair-coin-bayes.onrender.com).

## Prerequisites
You will need either Python 3.8 or 3.9. All required Python packages can be found in the `requirements.txt` file.

## Running the app locally
You may want to run the app using Flask locally before deploying it to Heroku, especially if you have made any changes to the code. To run locally:

1. clone the repository.
1. in the repository, run `make deploy-prod`.
1. open the link provided in the command line.

Alternatively, you can deploy using [Docker](https://www.docker.com/). You can run using `make docker-deploy` or
1. `docker build -t unfair-coin-bayes .`
1. `docker run --init --rm -d --publish 127.0.0.1:8000:8000 --env SECRET_KEY=$(bin/set-secret-key --) unfair-coin-bayes`

## License
This project is distributed under the MIT license. Please see `LICENSE` for more information.
