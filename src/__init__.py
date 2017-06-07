from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

from src.home.views import home_blueprint

# register our blueprints
app.register_blueprint(home_blueprint)