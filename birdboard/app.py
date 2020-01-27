from flask import Flask

from birdboard.blueprints.page import page
from birdboard.api.v1.projects import ProjectsView
from birdboard.extensions import (
    debug_toolbar,
    db,
    marshmallow
)


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__,  static_folder='../public', static_url_path='')

    app.config.from_object('config.settings')

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(page)

    ProjectsView.register(app)

    extensions(app)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    debug_toolbar.init_app(app)
    db.init_app(app)
    marshmallow.init_app(app)

    return None
