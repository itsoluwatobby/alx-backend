#!/usr/bin/env python3
"""Basic route task 1"""
from flask import Blueprint, render_template


app_routes = Blueprint('app_routes', __name__)


@app_routes.route('/', methods=['GET'], strict_slashes=False)
def home():
    """A basic endpoint that returns an home page"""
    return render_template('4-index.html')
