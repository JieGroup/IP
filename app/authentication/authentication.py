import jwt

from flask import g, current_app
from flask.json import jsonify
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from bson.json_util import loads, dumps

from datetime import datetime, timedelta, timezone

from app import pyMongo
from app.authentication import authentication_bp
from app.error import error_response
from app.authentication.utils import check_password
from app.utils.api import handle_response
from app.authentication.jwt import JwtManipulation

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@authentication_bp.route('/tokens', methods=['POST'])
@basic_auth.login_required
@handle_response
def get_token():
    
    '''
    Login function (doesnt need token). If the user registered but not confirmed yet, we lead it to the confirmation page.
    If the user finishes the confirmation, we send it a token.

    Parameters
    ----------
    None

    Returns
    -------
    dict[str, str]
    '''

    if g.current_user['confirm_email'] == False:
        msg = 'not verify email yet'
        return jsonify(msg)
    
    token = JwtManipulation.get_jwt(g.current_user)
    # print('token is', type(token), token)
    # print('token is 1', token.decode("utf-8"))
    # print('token is 2', dumps({'token': token.decode()}))
    # print('token is 3', jsonify(dumps({'token': token.decode()})))
    if isinstance(token, str):
        response = {
            'token': token
        }
    else:
        response = {
            'token': token.decode("utf-8")
        }
    return response

@basic_auth.verify_password
def verify_password(username, password):

    """
    check the username and password provided by the user

    Parameters:
        username - String.
        password - String

    Returns:
        Boolean

    Raises:
        KeyError - raises an exception
    """
    print('password')
    user = pyMongo.db.User.find_one({'username': username})
    if user is None:
        return False
    g.current_user = user
    return check_password(g.current_user, password)

@basic_auth.error_handler
def basic_auth_error():
    '''Return an error response in case of authentication failure'''
    return error_response(401)

@token_auth.verify_token
@handle_response
def verify_token(token):

    """
    check whether the user request has a token and validity of the token

    Parameters:
       token - object returned by jwt.decode()
       
    Returns:
        Boolean

    Raises:
        KeyError - raises an exception
    """

    print('token is!!!!!', token)

    g.current_user, token_payload = JwtManipulation.verify_jwt(token) if token else None

    if g.current_user:
        new_token = JwtManipulation.update_jwt(g.current_user, token_payload)
        g.current_user['new_token'] = new_token
    
    return g.current_user is not None

@token_auth.error_handler
@handle_response
def token_auth_error():
    '''Return an error response if Token Auth authentication fails'''
    return error_response(401)

