from flask_migrate import Migrate
from cimov.extensions.db import db

migrate = Migrate()

def init_app(app):
    migrate.init_app(app, db)