from flask import Flask, redirect, render_template, request
from bokeh_plot import create_plot

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
    script, div = create_plot(Pi=app.vars['probability'])
    return render_template('plot.html', Pi=app.vars['probability'], script=script, div=div)

if __name__ == '__main__':
    app.run(port=33507, debug=True)
