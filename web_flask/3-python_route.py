#!/usr/bin/python3
"""
Script that starts a Flask web application
3- Python is cool
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Returns a greeting message."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns a greeting message."""
    return "HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Returns 'C ' followed by the text variable with spaces replacing underscores."""
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Returns 'python ' followed by the text variable with spaces replacing underscores."""
    return f"python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
