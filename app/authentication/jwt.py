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


class JwtManipulation:

    '''
    jwt is Json Web Token. This class is the helper class
    for jwt manipulation

    Attributes
    ----------
    None

    Methods
    -------
    update_jwt
    get_jwt
    verify_jwt
    '''

    @classmethod
    def update_jwt(cls, user, token_payload, expires_in=5000):

        token_payload_expiration_time = token_payload.get('exp')

        # float
        current_time = datetime.now(tz=timezone.utc).timestamp()
        expiration_time = (datetime.now(tz=timezone.utc) + timedelta(seconds=expires_in)).timestamp()

        time_diff = abs(token_payload_expiration_time - current_time)
 
        # if the difference of time is greater than 10 mins, we dont update 
        # the token
        if time_diff > 1000:
            return None
        
        token_payload = {
            'user_id': user['user_id'],
            'user_name': user['name'] if 'name' in user else user['username'],
            'authority_level': user['authority_level'] if 'authority_level' in user else 'user',
            # expiration time
            'exp': expiration_time,
            # create time
            'iat': current_time
        }
  
        return jwt.encode(
            token_payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256')

    @classmethod
    def get_jwt(cls, user, expires_in=5000):
        current_time = datetime.now(tz=timezone.utc).timestamp()
        expiration_time = (datetime.now(tz=timezone.utc) + timedelta(seconds=expires_in)).timestamp()

        # float
        token_payload = {
            'user_id': user['user_id'],
            'user_name': user['name'] if 'name' in user else user['username'],
            'authority_level': user['authority_level'] if 'authority_level' in user else 'user',
            # expiration time
            'exp': expiration_time,
            # create time
            'iat': current_time
        }

        # print('type', type(jwt))
        # return jwt.encode(
        #     token_payload,
        #     current_app.config['SECRET_KEY'],
        #     algorithm='HS256').decode('utf-8')
        # a = jwt.encode(
        #     token_payload,
        #     current_app.config['SECRET_KEY'],
        #     algorithm='HS256')
        # print('aaaaaa', a, type(a))

        return jwt.encode(
            token_payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256')

    @classmethod
    def verify_jwt(cls, token):
        try:
            token_payload = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256'])
        except (jwt.exceptions.ExpiredSignatureError,
                jwt.exceptions.InvalidSignatureError,
                jwt.exceptions.DecodeError) as e:
            # If the Token expires or is modified by someone, the signature verification will also fail.
            return None, None
        
        user_id = token_payload.get('user_id')
        user_document = pyMongo.db.User.find_one({'user_id': user_id})
        return user_document, token_payload
