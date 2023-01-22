from flask import Flask

from settings import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import api_error_handlers, api_views, forms, models, utils, validators,views_error_handlers, views
