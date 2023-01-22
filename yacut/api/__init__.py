from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

from . import api_error_handlers, api_views