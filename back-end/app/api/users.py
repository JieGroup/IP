from __future__ import annotations

import re
import werkzeug
from bson import ObjectId

from flask.json import jsonify
from flask.helpers import url_for
from flask import request, g, render_template, flash

# from Items import db
from app import pyMongo

from app.authentication.api import (
    basic_auth,
    token_auth
)

from app.process.api import User

from app.api import api

from app.database.api import (
    search_document
)

from app.utils.api import Constant

from app.utils.api import handle_response

from app.api.utils import (
    check_if_data_is_valid,
    get_user_id_from_token,
    is_request_user_id_valid
)

from typing import Any


@api.route('/create_user', methods=['POST'])
@handle_response
def create_user() -> dict:
    '''
    Register new user
    1. Check if the username and the email are valid
    2. send email confirmation link to user input email

    Parameters
    ----------
    username : str
        username
    email : str
        email
    password : str
        password

    Returns
    -------
    dict

    Notes
    -----
    1. username must be unique
    2. email and password can be duplicate
    '''
    data = request.get_json()
    if not data:
      raise ValueError('No data. Please import JSON data')

    expected_data = {
        'username': str,
        'email': str,
        'password': str,
    }
    check_if_data_is_valid(
        data=data,
        expected_data=expected_data
    )
    if not re.match(Constant.EMAIL_PATTERN, data['email']):
        raise ValueError('Please provide a valid email address.')

    username = data['username']
    email = data['email']
    password = data['password']    
    return User.create_user(
        username=username,
        email=email,
        password=password,
    )


@api.route('/resend_email_confirmation_link/', methods=['POST'])
@handle_response
def resend_email_confirmation_link() -> dict:
    '''
    Resend the email confirmation link to user's email

    Parameters
    ----------
    None

    Returns
    -------
    dict
    '''
    data = request.get_json()
    if not data:
        raise ValueError('No data. Please import JSON data')
    
    expected_data = {
        'username': str,
        'email': str,
    }
    check_if_data_is_valid(
        data=data,
        expected_data=expected_data
    )

    username = data['username']
    email = data['email']
    return User.resend_email_confirmation_link(
        username=username,
        email=email
    )

@api.route('/confirm_email/<token>', methods=['GET'])
@handle_response
def confirm_email(token):
    '''
    After user clicking the confirmation link in the email,
    jump to this function.
        1. Check token and update corresponding user document
        2. return corresponding template and msg result

    Parameters
    ----------
    token : str
        unique str generated by URLSafeTimedSerializer.

    Returns
    -------
    str
        render_template would change html to special
        format str
    '''
    msg = User.confirm_email(
        token=token
    )
    return render_template('confirm.html', msg=msg)

@api.route('/get_own_info', methods=['GET'])
@token_auth.login_required
@handle_response
def get_own_info() -> dict:
    '''
    Request to get information about the user itself

    Parameters
    ----------
    None

    Returns
    -------
    dict
    '''
    return User.get_own_info()

@api.route('/reset_pwd', methods=['POST'])
@handle_response
def reset_pwd() -> dict:
    '''
    Reset the password

    Parameters
    ----------
    username : str
        username
    email : str
        email
    password : str
        password

    Returns
    -------
    dict
    '''
    data = request.get_json()
    if not data:
        raise ValueError('No data. Please import JSON data')
    
    expected_data = {
        'username': str,
        'email': str,
        'password': str,
    }
    check_if_data_is_valid(
        data=data,
        expected_data=expected_data
    )
    if not re.match(Constant.EMAIL_PATTERN, data['email']):
        raise ValueError('Please provide a valid email address.')
    
    username = data['username']
    email = data['email']
    password = data['password']
    return User.reset_pwd(
        username=username,
        email=email,
        password=password
    )


@api.route('/update_new_pwd/<string:token>', methods=['POST', 'GET'])
# @handle_response
def update_new_pwd(token) -> Any:
    '''
    Update new password

    Parameters
    ----------
    token : str
        token

    Returns
    -------
    Any
    '''
    print('jin update_new_pwd')
    if request.method == 'POST':
        print('~~~post', request, dir(request))
        print('>??', request.form, type(request.form) == werkzeug.datastructures.ImmutableMultiDict)
        if type(request.form) == werkzeug.datastructures.ImmutableMultiDict:
            data_form = request.form.to_dict()
        else:
            data_form = request.form
        
        # would have a "\" append in the end
        token = data_form['token']
        print('~~~post', request, token)
    # print('update_new_pwd', request, request.method)
    return User.update_new_pwd(
        token=token,
        request=request
    )


@api.route('/delete_user/<string:id>', methods=['DELETE'])
@token_auth.login_required
@handle_response
def delete_user(id):
    '''
    Delete a User. Implement Later
    '''
    return "Welcome to Delete!"




# @api.route('/update_user', methods=['POST'])
# @token_auth.login_required
# @handle_response
# def update_user():
#     '''
#     update user information

#     Parameters
#     ----------
#     user_id : str
#         user_id

#     Returns
#     -------
#     None
#     '''
#     data = request.get_json()
#     if not data:
#         raise ValueError('No data. Please import JSON data')

#     elif 'username' not in data or not data.get('username', None) or (' ' in data.get('username')):
#         raise ValueError('Please provide a valid username.')
#     pattern = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
#     if 'email' not in data or not re.match(pattern, data.get('email', None)) or (' ' in data.get('email')):
#         raise ValueError('Please provide a valid email address.')

#     cur_user_id = get_user_id_from_token()

#     # check if the caller of the function and the request user id is the same
#     if not is_request_user_id_valid(
#         cur_user_id=cur_user_id,
#         request_user_id=request_user_id
#     ):  
#         raise ValueError('wrong request user id')

#     username = data['username']
#     email = data['email']
    
#     return User.update_user(
#         user_id=cur_user_id,
#         username=username,
#         email=email,
#     )