from flask import Flask

from settings import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .api import api as api_blueprint
app.register_blueprint(api_blueprint)
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from . import models, utils
