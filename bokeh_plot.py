# TO DO:
# 1.) add area under curve
# 2.) add updated heads and tails
# 3.) add stats
# 5.) add comments!
# 6) clean imports

import numpy as np
import random

from bokeh.embed import components
from bokeh.layouts import column
from bokeh.plotting import Figure, show
from bokeh.models import ColumnDataSource, CustomJS, Patch
from bokeh.models.widgets import Button, DataTable, PreText, TableColumn


def create_plot(Pi):
    n = 1000
    x = np.linspace(0, 1, n)
    p = np.ones(n)

    a = 1
    b = 1

    s1 = ColumnDataSource(data=dict(x=x, p=p))
    s2 = ColumnDataSource(data=dict(params=[Pi, a, b]))

    plot = Figure()
    plot.xaxis.axis_label = 'Probability of Heads (-)'
    plot.yaxis.axis_label = 'Probability Density (-)'

    plot.line('x', 'p', source=s1, line_width=4)

    # patch = Patch(x='x', y='p', fill_color='#a6cee3')
    # plot.add_glyph(s1, patch)

    with open('callback.js', 'r') as fp:
        code = fp.read()

    callback = CustomJS(args=dict(s1=s1, s2=s2), code=code)
    button = Button(label='Flip Coin', callback=callback)
    layout = column(button, plot)

    return components(layout)


if __name__ == '__main__':
    script, div = create_plot()
