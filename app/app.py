import os

from bokeh import __version__
from flask import Flask, redirect, render_template, request, url_for

from app.forms import ProbabilityForm
from app.prob_dist import create_plot

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)


@app.route('/', methods=['GET', 'POST'])
def main():
    form = ProbabilityForm()

    if form.validate_on_submit():
        return plot()

    # The uniform prior is checked by default, hiding the beta distribution
    # parameters. Thus, an invalidated form where beta prior had been checked
    # would not show the selection. This insures the style for the prior
    # parameters are set to be shown.
    if form.prior.data == 'Beta':
        style = '"display: inline;"'
    else:
        style = '"display: none;"'

    return render_template('index.html', form=form, style=style)


def plot():
    form = ProbabilityForm(request.form)
    true_prob = form.probability.data
    param_a = form.param_a.data
    param_b = form.param_b.data

    script, div = create_plot(true_prob, param_a, param_b)

    return render_template(
        'plot.html',
        script=script,
        div=div,
        version=__version__
    )


if __name__ == '__main__':
    app.run()
