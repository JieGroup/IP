from __future__ import annotations

from flask import g

from flask import request

from flask_httpauth import HTTPTokenAuth

from app.utils.api import handle_response

from app.database.api import search_document

from app.authentication import authentication_bp
from app.authentication.basic_auth import basic_auth
from app.authentication.utils import has_user_confirmed_email
from app.authentication.jwt import JwtManipulation
from typeguard import typechecked

from app._typing import MTurkID


token_auth = HTTPTokenAuth()

@authentication_bp.route('/get_userToken', methods=['POST'])
@basic_auth.login_required
@handle_response
def get_userToken() -> None:
    '''
    When user login its account:
        1. pass the verification of username and password(decorator)
        2. get userToken based on user_id, username, authority_level, 
            expiration_time, and current_time

    Parameters
    ----------
    None

    Returns
    -------
    None

    Notes
    -----
    token will be handled in the handle_response
    '''
    if not has_user_confirmed_email(
        cur_user_info=g.current_user
    ):  
        raise ValueError('not verify email yet')
    
    userToken = JwtManipulation.get_jwt(
        role='user',
        cur_user_info=g.current_user
    )
    g.userToken = userToken
    return 

# @authentication_bp.route('/get_voter_token', methods=['POST'])
def get_voterToken(
    survey_template_id: str,
    mturk_id: MTurkID,
) -> None:
    '''
    Form voterToken based on survey_template_id
    and mturk_id, which contrains the voter can
    only answer current template

    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    voterToken = JwtManipulation.get_jwt(
        role='voter',
        cur_user_info={
            'survey_template_id': survey_template_id,
            'mturk_id': mturk_id
        }
    )
    
    g.voterToken = voterToken
    return None


@token_auth.verify_token
@typechecked
def verify_token(
    token: str
) -> bool:
    '''
    1. Check if the request contains token.
    2. Check the validity of the token
    3. Check if we need to update the token

    Parameters
    ----------
    None

    Returns
    -------
    bool
    '''
    if not JwtManipulation.verify_jwt(token=token):
        raise ValueError('token is not valid')
    
    token_payload = JwtManipulation.decode_jwt(token=token)
    
    # decide the role of token
    role = None
    if 'user_id' in token_payload:
        role = 'user'
    else:
        role = 'voter'
    
    if role == 'user':
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
                role=role,
                token_payload=token_payload,
                cur_user_info=g.current_user, 
            )
        g.userToken = token
    elif role == 'voter':
        if JwtManipulation.is_jwt_needing_update(
            token_payload=token_payload
        ):
            token = JwtManipulation.update_jwt(
                role=role,
                token_payload=token_payload,
            )
        g.voterToken = token
    return True