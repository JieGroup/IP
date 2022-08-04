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

# @basic_auth.verify_password
@typechecked
def verify_password(
    username: str, 
    password: str
) -> None:
    '''
    verify username and password

    Parameters
    ----------
    username : str
    password : str

    Returns
    -------
    None
    '''
    print('11')
    user_document = search_document(
        database_type='user',
        username=username,
    )
    print('22')
    if not is_password_valid(
        hashed_password=user_document['hashed_password'],
        password=password
    ):
        raise ValueError('password wrong')
    print('33')
    g.current_user = user_document
    return