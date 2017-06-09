from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

import src.views
from src.home.views import home_blueprint
from src.todo_list.views import todo_list_blueprint

# register our blueprints
app.register_blueprint(home_blueprint)
app.register_blueprint(todo_list_blueprint)