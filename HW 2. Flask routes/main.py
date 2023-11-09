from flask import Flask

from utils import generate_names

app = Flask(__name__)

@app.route("/Open_a_file")
def open_file():
    return open_requirements()

@app.route("/Names")
def names():
    return generate_names()

@app.route("/People_in_Space")
def people_in_space():
    return people_in_space()


if __name__ == "__main__":
    app.run(host="0.0.0.0")