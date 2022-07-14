from flask import Blueprint

authentication_bp = Blueprint('authentication', __name__, url_prefix='/auth')

from app.authentication.api import (
    basic_auth,
    token_auth
)
# if g.current_user != post.author and not g.current_user.can(Permission.ADMIN):
#         return error_response(403)