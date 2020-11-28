from bokeh import __version__
from flask import Flask, render_template, request

from unfair_coin_bayes.prob_dist import create_plot

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/plot', methods=['POST'])
def plot():
    true_prob = float(request.form['probability'])

    # Define distribution parameters based on chosen prior
    if request.form['prior'] == 'uniform':
        a_prior = 1
        b_prior = 1
    else:
        a_prior = int(request.form['a'])
        b_prior = int(request.form['b'])

    script, div = create_plot(true_prob, a_prior, b_prior)

    return render_template('plot.html',
                           script=script, div=div, version=__version__)


if __name__ == '__main__':
    app.run()
