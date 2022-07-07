from __future__ import annotations

from flask import g

from flask_httpauth import HTTPTokenAuth

from app.utils.api import handle_response

from app.database.api import search_document

from app.authentication import authentication_bp
from app.authentication.basic_auth import basic_auth
from app.authentication.utils import has_user_confirmed_email
from app.authentication.jwt import JwtManipulation
from typeguard import typechecked

token_auth = HTTPTokenAuth()

@authentication_bp.route('/get_user_tokens', methods=['POST'])
@basic_auth.login_required
def get_user_tokens() -> dict[str, str]:
    
    '''
    When user login its account:
        1. pass the verification of username and password(decorator)
        2. get token 

    Parameters
    ----------
    None

    Returns
    -------
    dict[str, str]
    '''

    if not has_user_confirmed_email(
        cur_user_info=g.current_user
    ):  
    # TODO: raise error
        msg = 'not verify email yet'
        return msg
    
    token = JwtManipulation.get_jwt(
        cur_user_info=g.current_user
    )

    return {
        'token': token
    }

@authentication_bp.route('/get_voter_tokens', methods=['POST'])
# @handle_response
def get_voter_token() -> dict[str, str]:
    
    '''
    When voter starts answering the topics:
        1. Since voter does not need to login, we dont need to 
            verify username and password.
        2. get token 

    Parameters
    ----------
    None

    Returns
    -------
    dict[str, str]
    '''

    if not has_user_confirmed_email(
        cur_user_info=g.current_user
    ):  
    # TODO: raise error
        msg = 'not verify email yet'
        return msg
    
    token = JwtManipulation.get_jwt(
        cur_user_info=g.current_user
    )

    return {
        'token': token
    }

@token_auth.verify_token
# @handle_response
@typechecked
def verify_token(
    token: str
) -> bool:

    '''
    1. Check if the request contains token.
    2. Check the validity of the token

    Parameters
    ----------
    None

    Returns
    -------
    bool
    '''

    if not JwtManipulation.verify_jwt(token=token):
        # TODO: raise error
        return None
    
    token_payload = JwtManipulation.decode_jwt(token=token)

    user_id = token_payload['user_id']
    user_document = search_document(
        database_type='user',
        user_id=user_id
    )
    g.current_user = user_document
    
    if JwtManipulation.is_jwt_needing_update(
        token_payload=token_payload
    ):
        token = JwtManipulation.update_jwt(
            cur_user_info=g.current_user, 
            token_payload=token_payload 
        )

    g.current_user['token'] = token
    return True

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

