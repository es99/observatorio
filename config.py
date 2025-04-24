import os

class Config:
    TITLE = 'cimov'
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    @staticmethod
    def init_app(app):
        pass
    
class DevelopmentConfig(Config):
    DEBUG = True
    
config = {
    'development': DevelopmentConfig
}