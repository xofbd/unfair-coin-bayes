[![Build Status](https://travis-ci.com/xofbd/unfair-coin-bayes.svg?branch=master)](https://travis-ci.com/xofbd/unfair-coin-bayes)
![Python 3.7](https://badgen.net/badge/Python/3.7/purple)
![Python 3.8](https://badgen.net/badge/Python/3.8/purple)
[![GitHub release](https://img.shields.io/github/v/release/xofbd/unfair-coin-bayes.svg)](https://github.com/xofbd/unfair-coin-bayes/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# Unfair Coin Bayesian Simulation
This repository creates a web app that simulates the evolving probability distribution of an unfair coin to come up heads using Bayes's theorem. The prior distribution is a Beta distribution with both shape parameters set to one, resulting in a uniform distribution. This repository is ready to deploy a web application using [Flask](https://flask.palletsprojects.com) and [Bokeh](https://bokeh.org) to Heroku. An example of the app can be seen at https://unfair-coin-bayes.herokuapp.com.

## Prerequisites
You will need either Python 3.7 or 3.8. All required Python packages can be found in the `requirements.txt` file. You will also need a Heroku account and have installed the Heroku CLI. For more information on the Heroku CLI, go to https://devcenter.heroku.com/articles/heroku-cli#download-and-install.

## Running the app locally using Flask
You may want to run the app using Flask locally before deploying it to Heroku, especially if you have made any changes to the code. To run locally:

1. clone the repository.
1. in the repository, run `make deploy-prod`.
1. open the link provided in the command line.

If you are using Windows, you can:
1. create and activate the virtual environment.
1. `set FLASK_APP="unfair_coin_bayes/app.py"` in the command line.
1. run `python -m flask run`.
1. open the link in the command line.

Alternatively, you can deploy using [Docker](https://www.docker.com/). You can run using `make docker-deploy` or
1. `docker build -t unfair_coin_bayes .`
1. `docker run -d -p 5000:5000 unfair_coin_bayes`

## Deploying to Heroku
Make sure your app is ready to be deployed to Heroku by running Flask locally. To deploy to Heroku:

1. clone the repository (if you haven't yet).
1. `heroku login` and enter your credentials.
1. `heroku create` or `heroku create app-name` where app-name is a custom app name.
1. `git push heroku master`.
1. `heroku open` or open the app online through your Heroku profile.

## License
This project is distributed under the MIT license. Please see `LICENSE` for more information.
