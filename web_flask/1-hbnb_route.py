#!/usr/bin/python3
"""script starts web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """first route handler """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnh():
    """ secodn route handler """

    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
