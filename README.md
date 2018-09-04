# Unfair Coin Bayesian Simulation
This repository creates a web app that simulates the evolving probability distribution of an unfair coin to come up heads using Bayes's theorem. The prior distribution is a Beta distribution with both shape parameters set to one, resulting in a uniform distribution. This repository is ready to deploy a Bokeh figure on Heroku. An exmaple of the app can be seen at https://tdi-ml-unfair-coin.herokuapp.com <br>

## Prerequisites
You will need to have these Python packages installed: <br>
`bokeh, Flask` <br>
You can easily download and install them by running `pip install package-name`, where "package-name" is the name of the desired package. You will also need a Heroku account and have installed the Heroku CLI. For more information on the Heroku CLI, go to https://devcenter.heroku.com/articles/heroku-cli#download-and-install.

## Running the app locally using Flask
You may want to run the app using Flask locally before deploying it to Heroku, especially if you have made any changes to the code. To run locally: <br>

0.) clone repository: `git clone https://github.com/xofbd/unfair-coin-bayes` <br>
1.) in the cloned directory, run `export FLASK_APP=app.py` in the command line. If you are using Windows, replace `export` with `set` <br>
2.) run `python -m flask run` <br>
3.) open the link provided in the command line <br>
For more information on running Flask, go to http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application <br>

## Deploying to Heroku
Make sure your app is ready to be deployed to Heroku by running Flask locally. To deploy to Heroku: <br>

0.) clone repository (if you haven't yet): `git clone https://github.com/xofbd/unfair-coin-bayes` <br>
1.) `heroku login` and enter your credentials <br>
2.) `heroku create` or `heroku create app-name` where app-name is a custom app name <br>
3.) `git push heroku master` <br>
4.) `heroku open` or open the app online through your Heroku profile <br>

## License
This project is distributed under the MIT license. Please see `LICENSE` for more information.