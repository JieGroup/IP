from __future__ import annotations

import jwt

from flask import current_app

from typeguard import typechecked

from app.utils.api import (
    Constant,
    Time
)

from typing import Union

from app._typing import Role


@typechecked
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
    def __form_userToken(
        cls,
        user_id: str,
        username: str,
        authority_level: str,
        exp: int,
        iat: int
    ) -> dict[str, Union[int, str]]:

        return {
            'user_id': user_id,
            'username': username,
            'authority_level': authority_level,
            'exp': exp,
            'iat': iat
        }

    @classmethod
    def __form_voterToken(
        cls,
        survey_template_id: str,
        mturk_id: str,
        authority_level: str,
        exp: int,
        iat: int
    ) -> dict[str, Union[int, str]]:

        return {
            'survey_template_id': survey_template_id,
            'mturk_id': mturk_id,
            'authority_level': authority_level,
            'exp': exp,
            'iat': iat
        }

    @classmethod
    def update_jwt(
        cls, 
        role: Role,
        token_payload: dict, 
        cur_user_info: dict=None, 
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
        new_expiration_time = Time.get_expiration_utc_time(time_period=expires_in)
        
        # exp is token expiration time
        # iat is token create time
        token_payload = None
        if role == 'user':
            token_payload = cls.__form_userToken(
                user_id=cur_user_info['user_id'],
                username=cur_user_info['username'],
                authority_level=cur_user_info['authority_level'] if 'authority_level' in cur_user_info else 'user',
                exp=new_expiration_time,
                iat=current_time
            )
        elif role == 'voter':
            token_payload = cls.__form_voterToken(
                survey_template_id=token_payload['survey_template_id'],
                mturk_id=token_payload['mturk_id'],
                authority_level='voter',
                exp=new_expiration_time,
                iat=current_time
            )
        else:
            raise ValueError('role is not belonged to user or voter')

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
        role: Role,
        cur_user_info: dict, 
        expires_in: int=Constant.TOKEN_EXPIRATION_PERIOD
    ) -> str:
        '''
        Get token

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
        token_payload = None
        if role == 'user':
            token_payload = cls.__form_userToken(
                user_id=cur_user_info['user_id'],
                username=cur_user_info['username'],
                authority_level=cur_user_info['authority_level'] if 'authority_level' in cur_user_info else 'user',
                exp=expiration_time,
                iat=current_time
            )
        elif role == 'voter':
            token_payload = cls.__form_voterToken(
                survey_template_id=cur_user_info['survey_template_id'],
                mturk_id=cur_user_info['mturk_id'],
                authority_level='voter',
                exp=expiration_time,
                iat=current_time
            )
        else:
            raise ValueError('role is not belonged to user or voter')
        
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

    @classmethod
    def decode_jwt(
        cls,
        token: str
    ) -> dict:
        '''
        Decode token

        Parameters
        ----------
        token : str
            token

        Returns
        -------
        str
        '''
        token_payload = jwt.decode(
            token,
            current_app.config['SECRET_KEY'],
            algorithms=['HS256']
        )
        return token_payload