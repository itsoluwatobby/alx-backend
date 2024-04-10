#!/usr/bin/env python3
"""
setup a basic Flask app in 0-app.py. Create a single / route
and an index.html
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """A basic endpoint that returns an home page"""
    title = "Welcome to Holberton"
    return render_template('0-index.html', title=title)


if __name__ == "__main__":
    """Runs the basic flask app"""
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
