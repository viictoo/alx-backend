#!/usr/bin/env python3
"""basic flask app with  Parametrized templates"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """config settings for babel i18n
    Args:
        object (obj): instance of a class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """determine the best match with our
    supported languages

    Returns:
        str: best language match
        """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', strict_slashes=False)
def root():
    """base route

    Returns:
        template: page presentation
    """
    return render_template('3-index.html')
