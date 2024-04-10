#!/usr/bin/env python3
"""Basic Flask app with Babel"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

app = Flask(__name__)
babel = Babel(app)

class Config:
    """
    Configuration class for flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)   

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """
    Retrieve a user dict or None if ID not found
    """
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None

@app.before_request
def before_request_func():
    """
    Set user info globally before any request
    """
    g.user = get_user()

@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match with our supported languages
    """
    if 'locale' in request.args and request.args.get['locale'] in Config.LANGUAGES:
        return request.args.get['locale']
    user = g.get('user', None)
    if user and user.get('locale') in Config.LANGUAGES:
        return user.get('locale')        
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone():
    """
    Determine the best match for timezone
    """
    if 'timezone' in request.args:
        try:
            return ptyz.timezone(request.args['timezone']).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    user = g.get('user', None)
    if user and user.get('timezone'):
        try:
            return pytz.timezone(user.get('timezone')).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return 'UTC'

@app.route('/')
def index():
    """
    Render the index page
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    