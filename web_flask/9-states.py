#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects in DBStorage.
    /states/<id>: HTML page with information about a specific State.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage."""
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def state_info(id):
    """Displays an HTML page with information about a specific State."""
    state = storage.get("State", id)
    if state:
        return render_template("9-states.html", state=state)
    else:
        return render_template("9-states.html", not_found=True)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
