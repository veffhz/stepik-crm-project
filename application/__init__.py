from flask import Flask

from config import Config
from application.extensions import db, migrate, csrf
from application.extensions import admin_manager, login_manager

app = Flask(__name__)


def create_app(config_class=Config):
    app.config.from_object(config_class)
    from application import controllers
    from application.models import db, User
    from application.admin import init_admin
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    login_manager.init_app(app)
    admin_manager.init_app(app)
    init_admin(admin_manager)
    authentication(User)
    return app


def authentication(user_model):
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(uid):
        return user_model.query.get(uid)
