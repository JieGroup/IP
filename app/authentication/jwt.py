from __future__ import annotations

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

from app.utils.api import (
    Constant,
    Time
)

from typing import Union


class JwtManipulation:

    '''
    jwt is Json Web Token. This class is the helper class
    for jwt manipulation

    Attributes
    ----------
    None

    Methods
    -------
    is_jwt_needing_update
    update_jwt
    get_jwt
    verify_jwt
    '''

    @classmethod
    def is_jwt_needing_update(
        cls,
        current_time: float, 
        
        token_payload: dict,
    ) -> bool:

        '''
        Time difference is token_payload_expiration_time - current_time
        if time difference is greater than Constant.UPDATE_TOKEN_INTERVAL,
        we dont need to update token yet.
        If time difference is smaller than 0, the token has been expired.

        Parameters
        ----------
        time_diff : int
            Time difference between the current time and the token 
            expiration time.
        
        Returns
        -------
        dict[str, str]
        '''

        current_time = Time.get_current_utc_time()
        token_payload_expiration_time = token_payload.get('exp')

        time_diff = token_payload_expiration_time - current_time
        if time_diff > Constant.UPDATE_TOKEN_INTERVAL:
            return False
        if time_diff < 0:
            return False
    
        return True

    @classmethod
    def __change_token_to_str(
        cls, token: Union[str, bytes]
    ) -> str:

        '''
        jwt.encode has some compatible issue with python version. 
        The return value may be str or bytes type

        Parameters
        ----------
        token : Union[str, bytes]
            token
        
        Returns
        -------
        str
        '''

        if not isinstance(token, str):
            return token.decode("utf-8")
        
        return token

    @classmethod
    def update_jwt(
        cls, 
        cur_user_info: dict, 
        token_payload: dict, 
        expires_in: int=Constant.TOKEN_EXPIRATION_PERIOD
    ) -> str:

        '''
        Update jwt when the expiration time is close to 
        current time (Currently set to 15 mins)

        Parameters
        ----------
        cur_user_info : dict
        token_payload : dict
        expires_in : int

        Returns
        -------
        dict[str, str]
        '''

        current_time = Time.get_current_utc_time()
        token_payload_expiration_time = token_payload.get('exp')

        if not cls.__is_jwt_needing_update(
            current_time=current_time,
            token_payload_expiration_time=token_payload_expiration_time
        ):
            return None
        
        new_expiration_time = Time.get_expiration_utc_time(time_period=expires_in)
        # exp is token expiration time
        # iat is token create time
        token_payload = {
            'user_id': cur_user_info['user_id'],
            'username': cur_user_info['name'] if 'name' in cur_user_info else cur_user_info['username'],
            'authority_level': cur_user_info['authority_level'] if 'authority_level' in cur_user_info else 'user',
            'exp': new_expiration_time,
            'iat': current_time
        }

        token = jwt.encode(
            token_payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )

        return cls.__change_token_to_str(
            token=token
        )


    @classmethod
    def get_jwt(
        cls, 
        cur_user_info: dict, 
        expires_in: int=Constant.TOKEN_EXPIRATION_PERIOD
    ) -> None:

        '''
        get token

        Parameters
        ----------
        cur_user_info : dict
        expires_in : int
            TOKEN_EXPIRATION_TIME

        Returns
        -------
        dict[str, str]
        '''

        current_time = Time.get_current_utc_time()
        expiration_time = Time.get_expiration_utc_time(
            time_period=expires_in
        )

        # exp is token expiration time
        # iat is token create time
        token_payload = {
            'user_id': cur_user_info['user_id'],
            'username': cur_user_info['name'] if 'name' in cur_user_info else cur_user_info['username'],
            'authority_level': cur_user_info['authority_level'] if 'authority_level' in cur_user_info else 'user',
            'exp': expiration_time,
            'iat': current_time
        }

        token = jwt.encode(
            token_payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )
        
        return cls.__change_token_to_str(
            token=token
        )

    @classmethod
    def verify_jwt(
        cls, 
        token: str
    ) -> bool:

        '''
        Verify the token uploaded by the web

        Parameters
        ----------
        token : str
            token

        Returns
        -------
        bool
        '''

        try:
            token_payload = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256']
            )
        except (jwt.exceptions.ExpiredSignatureError,
                jwt.exceptions.InvalidSignatureError,
                jwt.exceptions.DecodeError) as e:
            # If the Token expires or is modified by someone, 
            # the signature verification will also fail.
            return False
        
        return True
        
        user_id = token_payload.get('user_id')
        user_document = pyMongo.db.User.find_one({'user_id': user_id})
        return user_document, token_payload

    @classmethod
    def decode_jwt(
        cls,
        token: str
    ) -> dict:

        token_payload = jwt.decode(
            token,
            current_app.config['SECRET_KEY'],
            algorithms=['HS256']
        )

        return token_payload