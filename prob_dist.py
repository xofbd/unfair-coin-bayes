from bokeh.embed import components
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.widgets import Button, Div, PreText
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

    Returns
    -------
    Script and div components of the Bokeh document.
    """

    # generate prior probability distribution
    n = 1000
    a = a_prior
    b = b_prior

    x = np.linspace(0, 1, n)
    dist = beta(a, b)
    p = dist.pdf(x)

    s1 = ColumnDataSource(data=dict(x=x, p=p))
    s2 = ColumnDataSource(data=dict(params=[Pi, a_prior, b_prior, a, b]))

    # arrays for the area under the curve patch
    xs = np.hstack((x, [1, 0]))
    ys = np.hstack((p, [0, 0]))
    s3 = ColumnDataSource(data=dict(x=xs, y=ys))

    # plot probability distribution
    plot = Figure(title='Posterior Distribution')
    plot.xaxis.axis_label = 'Probability of Heads (-)'
    plot.yaxis.axis_label = 'Probability Density (-)'
    plot.line('x', 'p', source=s1, line_width=4)
    plot.patch('x', 'y', source=s3, alpha=0.25, line_width=0)

    # calculate mode of prior
    if a == 1 and b == 1:
        mode_str = "any value"
    else:
        mode_str = str(round((a - 1.0) / (a + b - 2.0), 7))

    # add current stats of simulation
    text = """<b>True Probability:</b> {:g}<br>
              <b>Number of Heads:</b> {:d}<br>
              <b>Number of Tails:</b> {:d}<br>
              <b>Mode:</b> {:s}<br>
              <b>Variance: </b> {:g}
    """.format(Pi, a - a_prior, b - b_prior, mode_str, 1.0 / 12)
    div = Div(text=text)

    # create button widget and JS callback
    with open('callback.js', 'r') as fp:
        code = fp.read()

    callback = CustomJS(args=dict(s1=s1, s2=s2, s3=s3, div=div), code=code)
    button = Button(label='Flip Coin', callback=callback)

    # combine button and plot into one object and return components
    widgets = row(button, div)
    layout = column(widgets, plot)

    return components(layout)

if __name__ == '__main__':
    script, div = create_plot(0.5, 1, 1)
