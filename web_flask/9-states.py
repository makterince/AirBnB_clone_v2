#!/usr/bin/python3

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception=None):
    """ config """

    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """ config """

    states = sorted(storage.all("State").values(), 
                    ey=lambda state: state.name)
    return render_template('states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """ config """

    state = storage.get("State", id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('state.html', state=state, cities=cities)
    else:
        return render_template('not_found.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
