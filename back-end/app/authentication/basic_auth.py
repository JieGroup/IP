from __future__ import annotations

from flask import g, current_app
from flask.json import jsonify
from flask_httpauth import HTTPBasicAuth

from app import pyMongo

from app.utils.api import handle_response

from app.authentication.utils import is_password_valid

from typeguard import typechecked

basic_auth = HTTPBasicAuth()

@basic_auth.verify_password
@typechecked
def verify_password(
    username: str, 
    password: str
) -> bool:
    '''
    verify username and password

    Parameters
    ----------
    username : str
    password : str

    Returns
    -------
    bool
    '''
    user = pyMongo.db.User.find_one({'username': username})
    if user is None:
        raise ValueError('user cannot found')
    if not is_password_valid(
        hashed_password=g.current_user['hashed_password'],
        password=password
    ):
        raise ValueError('user cannot found')

    g.current_user = user
    return True

# @basic_auth.error_handler
# def basic_auth_error():
#     '''
#     Return an error response in case of authentication failure

#     Parameters
#     ----------
#     None

#     Returns
#     -------
#     TODO
#     '''
#     return error_response(401)