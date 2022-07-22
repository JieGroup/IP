from __future__ import annotations

from flask import g, current_app
from flask.json import jsonify
from flask_httpauth import HTTPBasicAuth

from app import pyMongo

from app.utils.api import handle_response

from app.database.api import search_document

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
    user = search_document(
        database_type='user',
        username=username,
    )
    if not is_password_valid(
        hashed_password=user['hashed_password'],
        password=password
    ):
        raise ValueError('password wrong')

    g.current_user = user
    return True