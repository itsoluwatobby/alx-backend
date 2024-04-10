#!/usr/bin/env python3
"""module 2-app.py"""
from flask import Flask, request
from flask_babel import Babel
from routes.route3 import app_routes
from config import Config
from typing import Union


app = Flask(__name__)
babel = Babel(app)


app.config.from_object(Config)
app.register_blueprint(app_routes)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """Determine best match for a supported languages
    """
    return request.accept_languages.best_match(config['LANGUAGES'])


if __name__ == "__main__":
    """Runs the basic flask app"""
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
