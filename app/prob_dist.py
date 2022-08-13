from pathlib import Path

from bokeh.embed import components
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.widgets import Button, Div
from bokeh.plotting import Figure
import numpy as np
from scipy.stats import beta


def create_plot(Pi, a_prior, b_prior):
    """Plots the prior probability distribution of an unfair coin using Bayes'
    theorem.

    Parameters
    ----------
    Pi : float
        Probability of the coin to come up heads.

    a_prior : int
        a parameter for the gamma prior distribution.

    b_prior : int
        b parameter for the gamma prior distribution.

    Returns
    -------
    Script and div components of the Bokeh document.
    """

    s1, s2, s3 = generate_prior_data(Pi, a_prior, b_prior)
    plot = create_figure(s1, s3)

    div = create_div_stats(Pi, a_prior, b_prior)
    widgets = create_coin_flip_button(s1, s2, s3, plot, div)
    layout = column(widgets, plot)

    return components(layout)


def generate_prior_data(Pi, a_prior, b_prior):
    """Return column data sources needed to generate prior distribution."""

    # Prior probability distribution
    n = 1000
    x = np.linspace(0, 1, n)
    dist = beta(a_prior, b_prior)
    p = dist.pdf(x)

    # Arrays for the area under the curve patch
    xs = np.hstack((x, [1, 0]))
    ys = np.hstack((p, [0, 0]))

    # Create column data sources
    s1 = ColumnDataSource(data={'x': x, 'p': p})
    s2 = ColumnDataSource(data={'params':
                                [Pi, a_prior, b_prior, a_prior, b_prior]})
    s3 = ColumnDataSource(data={'x': xs, 'y': ys})

    return s1, s2, s3


def create_figure(s1, s3):
    """Return figure object of probability distribution."""
    plot = Figure(title='Prior Distribution')
    plot.xaxis.axis_label = 'Probability of Heads (-)'
    plot.yaxis.axis_label = 'Probability Density (-)'
    plot.line('x', 'p', source=s1, line_width=4)
    plot.patch('x', 'y', source=s3, alpha=0.25, line_width=0)

    return plot


def create_div_stats(Pi, a, b):
    """Return div element with text of distribution statistics."""

    # Calculate mode and variance probability based on prior.
    if a == 1 and b == 1:
        mode_str = "any value"
    else:
        # str(round((a - 1.0) / (a + b - 2.0), 7))
        mode_str = f"{(a - 1.0) / (a + b - 2.0) :g}"

    var = a * b / ((a + b + 1) * (a + b)**2)

    # Add current stats of simulation
    text = f"""<b>True Probability:</b> {Pi :g}<br>
              <b>Number of Heads:</b> 0<br>
              <b>Number of Tails:</b> 0<br>
              <b>Mode:</b> {mode_str}<br>
              <b>Variance:</b> {var :g}"""

    return Div(text=text)


def create_coin_flip_button(s1, s2, s3, plot, div):
    """Return Bokeh widget with coin flip button."""

    # Create button widget and JS callback
    with open(Path('app') / 'static' / 'callback.js') as f:
        code = f.read()

    args = {'s1': s1, 's2': s2, 's3': s3, 'plot': plot, 'div': div}
    callback = CustomJS(args=args, code=code)
    button = Button(label='Flip Coin', callback=callback)

    # Combine button and div with stats into one row object
    widgets = row(button, div)

    return widgets


if __name__ == '__main__':
    script, div = create_plot(0.5, 1, 1)
