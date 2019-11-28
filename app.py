import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/index1', methods=['GET', 'POST'])
def index1():

    if request.method == 'POST':

        name = request.form.get('InputName')

        print(name)

    return render_template("index1.html", name=name)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
