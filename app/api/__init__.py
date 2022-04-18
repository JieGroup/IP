from flask import Blueprint

# use first bp in later version
# api_bp = Blueprint('api', __name__, url_prefix='/api')

# api_bp = Blueprint('api', __name__, template_folder='templates', static_folder='static')
api_bp = Blueprint('api', __name__, template_folder='templates')

from app.api import api