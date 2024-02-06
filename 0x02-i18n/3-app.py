#!/usr/bin/env python3
"""basic flask app with  Parametrized templates"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)


class Config(object):
    """config settings for babel i18n
    Args:
        object (obj): instance of a class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """determine the best match with our
    supported languages

    Returns:
        str: best language match
        """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


# babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def root():
    """base route

    Returns:
        template: page presentation
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
