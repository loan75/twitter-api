# app/__init__.py
# pylint: disable=missing-docstring

from flask import Flask
from .main.controllers import main


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)

    return app
