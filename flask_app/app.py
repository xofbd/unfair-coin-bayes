from flask import Flask, redirect, render_template, request
from flask_app.prob_dist import create_plot

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/plot', methods=['POST'])
def plot():
    params = {}
    params['probability'] = float(request.form['probability'])
    params['prior'] = request.form['prior']

    # Define distribution parameters based on chosen prior
    if params['prior'] == 'uniform':
        params['a_prior'] = 1
        params['b_prior'] = 1
    else:
        params['a_prior'] = int(request.form['a'])
        params['b_prior'] = int(request.form['b'])

    script, div = create_plot(params['probability'], params['a_prior'],
                              params['b_prior'])

    return render_template('plot.html', script=script, div=div)


if __name__ == '__main__':
    app.run(port=33507, debug=False)
