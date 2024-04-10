#!/usr/bin/env python3
"""module 5-app.py, Mock login"""
from flask import Flask, request, render_template, g
from flask_babel import Babel
from config import Config
from typing import Union
from os import getenv


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
babel = Babel(app)


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ GET /
    Return: 4-index.html
    """
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """ Determines best match for supported languages """
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[dict, None]:
    """ Returns user object if found """
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
    else:
        return None


@app.before_request
def before_request():
    """ Finds user and sets as global on flask.g.user """
    g.user = get_user()


@babel.localeselector
def get_locale() -> Union[str, None]:
    """Determines the best match supported languages
    """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(config['LANGUAGES'])


if __name__ == "__main__":
    """Runs the basic flask app"""
    app.run(debug=True)
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
