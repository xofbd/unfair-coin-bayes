from flask import Flask, redirect, render_template, request
from prob_dist import create_plot

app = Flask(__name__)
app.vars = {}


@app.route('/')
def main():
    return redirect('/index')


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/plot', methods=['POST'])
def plot():
    app.vars['probability'] = float(request.form['probability'])
    app.vars['prior'] = request.form['prior']

    # define distribution parameters based on chosen prior
    if app.vars['prior'] == 'uniform':
        app.vars['a_prior'] = 1
        app.vars['b_prior'] = 1
    else:
        app.vars['a_prior'] = int(request.form['a'])
        app.vars['b_prior'] = int(request.form['b'])

    script, div = create_plot(app.vars['probability'], app.vars['a_prior'],
                              app.vars['b_prior'])

    return render_template('plot.html', script=script, div=div)

if __name__ == '__main__':
    app.run(port=33507, debug=False)
