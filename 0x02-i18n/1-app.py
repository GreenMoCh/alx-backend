#!/usr/bin/env python3
"""Basic Flask app with Babel"""

from flask import Flask, render_template
from flask_babel import Babel

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

@app.route('/')
def index():
    """
    Render the index page
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    