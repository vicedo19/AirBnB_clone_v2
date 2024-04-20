#!/usr/bin/python3
"""
Script that starts a Flask web application
0- Hello Flask!
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Returns a greeting message."""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
