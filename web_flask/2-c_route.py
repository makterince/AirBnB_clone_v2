#!/usr/bin/python3
""" starts a flask web application """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ route handler """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ route handler """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """replace underscore with whitespace """
    format_text = text.replace('_', ' ')
    return f'C {format_text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
