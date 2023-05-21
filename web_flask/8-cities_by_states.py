#!/usr/bin/python3
""" script starts a web application """

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception=None):
    """ config """

    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ config """

    states = sorted(storage.all("State").values(),
                    key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
