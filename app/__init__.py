from logging import FileHandler, StreamHandler
from logging.config import dictConfig

import flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, current_user, login_required, logout_user
from flask_nav.elements import Navbar, View

from app.main import main
from app.nav import nav

from .repo.login_dao import select_user_byid

login_manager = LoginManager()

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    },
    'file': {'class': 'logging.FileHandler',
        'filename': 'status.log'
    }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi', 'file']
    }
})

@login_manager.user_loader
def load_user(user_id):
    return select_user_byid(user_id)

def create_app(test_config=None):
    app = flask.Flask(__name__)
    if test_config is not None:
        app.config.update(test_config)
    Bootstrap(app)
    nav.init_app(app)

    nav.register_element('frontend_top', Navbar(
    View('Project 1', '.index'),
    View('Home', '.login_page'),
    View('Login', '.login_page'),
    View('Logout', '.logout'),
    ))

    app.secret_key = '123456789'
       
    login_manager.login_view = '.login_page'
    login_manager.init_app(app)

    app.register_blueprint(main)

    return app
