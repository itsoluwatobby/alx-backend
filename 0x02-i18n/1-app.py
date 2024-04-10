#!/usr/bin/env python3
"""module 1-app.py"""
from flask import Flask
from flask_babel import Babel
from routes.route1 import app_routes


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """A language config class for babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
app.register_blueprint(app_routes)


if __name__ == "__main__":
    """Runs the basic flask app"""
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
