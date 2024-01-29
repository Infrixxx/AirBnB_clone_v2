from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def close_db_session(exception=None):
    storage.close()

@app.route('/')
def index():
    states = storage.all("State")
    return render_template("9-states.html", states=states)

@app.route('/states/<state_id>')
def state_details(state_id):
    state = storage.get("State", state_id)
    if state:
        cities = (
            state.cities  # Use cities relationship for DBStorage
            if storage._USER_DB == "db"
            else state.cities()  # Use cities getter for FileStorage
        )
        return render_template("9-states.html", state=state, cities=cities)
    else:
        return render_template("9-states.html", state=None), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
