import numpy as np

from bokeh.embed import components
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.widgets import Button, Div, PreText
from bokeh.plotting import Figure

from scipy.stats import beta


def create_plot(Pi):
    """Plots the prior probability distribution of an unfair coin using Bayes'
    theorem.

    Parameters
    ----------
    Pi : float
        Probability of the coin to come up heads.

    Returns
    -------
    Script and div components of the Bokeh document.
    """

    # generate prior probability distribution (uniform)
    n = 1000
    a = 1
    b = 1

    x = np.linspace(0, 1, n)
    dist = beta(a, b)
    p = dist.pdf(x)

    s1 = ColumnDataSource(data=dict(x=x, p=p))
    s2 = ColumnDataSource(data=dict(params=[Pi, a, b]))

    # plot probability distribution
    plot = Figure()
    plot.xaxis.axis_label = 'Probability of Heads (-)'
    plot.yaxis.axis_label = 'Probability Density (-)'
    plot.line('x', 'p', source=s1, line_width=4)

    # add current stats of simulation
    text = """<b>True Probability:</b> {:g}<br>
              <b>Number of Heads:</b> {:d}<br>
              <b>Number of Tails:</b> {:d}<br>
              <b>Mode:</b> {:s}<br>
              <b>Variance: </b> {:g}
    """.format(Pi, b - 1, a - 1, "any value", 1.0 / 12)
    div = Div(text=text)

    # create button widget and JS callback
    with open('callback.js', 'r') as fp:
        code = fp.read()

    callback = CustomJS(args=dict(s1=s1, s2=s2, div=div), code=code)
    button = Button(label='Flip Coin', callback=callback)

    # combine button and plot into one object and return components
    widgets = row(button, div)
    layout = column(widgets, plot)

    return components(layout)


if __name__ == '__main__':
    script, div = create_plot(0.5)
