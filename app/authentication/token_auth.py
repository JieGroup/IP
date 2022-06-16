from __future__ import annotations

from flask import g

from flask_httpauth import HTTPTokenAuth

from app.error import error_response

from app.utils.api import handle_response

from app.authentication import authentication_bp
from app.authentication.jwt import JwtManipulation

token_auth = HTTPTokenAuth()

@authentication_bp.route('/get_voter_tokens', methods=['POST'])
# @handle_response
def get_voter_token():
    
    '''
    Login function (doesnt need token). If the user registered but not confirmed yet, we lead it to the confirmation page.
    If the user finishes the confirmation, we send it a token.

    Since voter do not need to login, we dont need to verify username and password.

    Parameters
    ----------
    None

    Returns
    -------
    dict[str, str]
    '''

    if g.current_user['confirm_email'] == False:
        msg = 'not verify email yet'
        return msg
    
    token = JwtManipulation.get_jwt(g.current_user)

    return {
        'token': token
    }


@token_auth.verify_token
# @handle_response
def verify_token(
    token
) -> bool:

    '''
    Check if the request contains token.
    Check the validity of the token

    Parameters
    ----------
    None

    Returns
    -------
    bool
    '''

    print('token is!!!!!', token)

    if not JwtManipulation.verify_jwt(token=token):
        return None
    
    g.current_user = 
    token_payload = JwtManipulation.decode_jwt(token=token)

    if JwtManipulation.is_jwt_needing_update(
        token_payload=token_payload
    ):
        new_token = JwtManipulation.update_jwt(g.current_user, token_payload)

    g.current_user['new_token'] = new_token
    
    return g.current_user is not None

@token_auth.error_handler
@handle_response
def token_auth_error():

    '''
    Return an error response if Token Auth authentication fails

    Parameters
    ----------
    None

    Returns
    -------
    TODO
    '''

    return error_response(401)

