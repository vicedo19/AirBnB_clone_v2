#!/usr/bin/python3
"""
Script that starts a Flask web application
Is it a number?
"""
from flask import Flask, request

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return "C %s" % str(text.replace("_", " "))


@app.route("/python/<string:text>", strict_slashes=False)
@app.route("/python/")
def python(text="is_cool"):
    return "Python %s" % str(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def intCheck(n):
    return "%d is a number" % (n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
