from flask import Flask
from config import config
from cimov.blueprints import main
from cimov.blueprints import auth
from cimov.extensions import bootstrap
from cimov.extensions import db
from cimov.extensions import migrate
from cimov.extensions import login
from cimov.extensions import admin

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    main.init_app(app)
    auth.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    login.init_app(app)
    admin.init_app(app)
    
    return app