#!usr/bin/env python
""" Welcome to my tiny flask app"""

from flask import Flask

APP = Flask(__name__)

@APP.route("/")
def hello():
    """Returns default page"""
    return "Hello World"

if __name__ == "__main__":
    APP.run(debug=True)
    