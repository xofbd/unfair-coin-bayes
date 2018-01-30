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
    script, div = create_plot(app.vars['probability'])

    return render_template('plot.html', probability=app.vars['probability'],
                           script=script, div=div)

if __name__ == '__main__':
    app.run(port=33507, debug=True)
