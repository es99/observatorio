import os
from cimov.app import create_app

app = create_app(os.getenv('FLASK_CONFIG'))