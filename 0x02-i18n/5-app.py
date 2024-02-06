#!/usr/bin/env python3
"""Mock logging in with basic flask app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
app = Flask(__name__)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """config settings for babel i18n
    Args:
        object (obj): instance of a class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user():
    """ function that returns a user dictionary or None if
    the ID cannot be found or if login_as was not passed.
    """
    user = request.args.get('login_as')

    if user and int(user) in users.keys():
        return users.get(int(user))

    return None


@app.before_request
def before_request():
    """executed before all other functions
    identify and set a user session
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """determine the best match with our
    supported languages

    Returns:
        str: best language match
        """
    lang = request.args.get('locale')
    if lang and lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config["LANGUAGES"])

# babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def root():
    """base route

    Returns:
        template: page presentation
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
