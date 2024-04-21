#!/usr/bin/python3
"""
Script that starts a Flask web application
2- C is fun!
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
