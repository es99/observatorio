import os

class Config:
    TITLE = 'cimov'
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def init_app(app):
        pass
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flasky:flasky@127.0.0.1/cimov'
    
config = {
    'development': DevelopmentConfig
}