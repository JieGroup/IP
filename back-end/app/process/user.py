from __future__ import annotations

from bson import ObjectId

from typing import (
    Any,
    Union
)

from app.database.api import (
    search_document,
    create_document,
    update_document
)

from app.process.utils import (
    get_hashed_password,
    get_unique_id,
    validate_password,
    generate_confirmation_token,
    send_email,
    get_user_id_from_token,
    if_token_user_id_equals_user_id,
    is_token_matched,
    decode_token
)

from typeguard import typechecked

from flask.helpers import url_for

from flask import (
    request, 
    g, 
    render_template, 
    flash
)


@typechecked
class User:
    '''
    Handle the user-related information

    Attributes
    ----------
    None

    Methods
    -------
    create_user
    get_user
    update_user
    '''

    @classmethod
    def create_user(
        cls,
        username: str,
        email: str,
        password: str,
    ) -> None:
        '''
        Handle creating new account

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
        bool
        '''
        # Check if the username is duplicated
        user_document = search_document(
            database_type='user',
            check_response=False,
            username=username
        )
        if user_document:
            raise ValueError('Please use a different username.')
        
        validate_password_indicator, return_message = validate_password(password)
        if not validate_password_indicator:
            raise ValueError(f'{return_message}')
        
        user_id = get_unique_id()
        hashed_password = get_hashed_password(password)
        create_document(
            database_type='user',
            user_id=user_id,
            username=username,
            email=email,
            hashed_password=hashed_password,
            confirm_email=False,
            created_template={}
        )
        
        token = generate_confirmation_token(email)
        confirm_url = url_for(
            'api.confirm_email', 
            token=token, 
            _external=True
        )
        html_template = render_template('activate.html', confirm_url=confirm_url)
        message = "Please confirm your email"
        send_email(
            target_email=email, 
            message=message, 
            html_template=html_template
        )
        response = {}
        response['token'] = token
        response['message'] = 'create successfully'
        return response

    @classmethod
    def get_user(
        cls, user_id: str
    ) -> None:
        '''
        Request to get information about the user_id

        Parameters
        ----------
        user_id : str
            Unique user_id

        Returns
        -------
        dict
        '''
        token_user_id = get_user_id_from_token()
        if if_token_user_id_equals_user_id(
            token_user_id=token_user_id,
            user_id=user_id
        ):
            current_user_information = g.current_user
            # delete ObjectID to jsonify
            del current_user_information['_id']
            return {
                'user': current_user_information
            }
        else:
            raise ValueError('Wrong UserId')    
    
    @classmethod
    def update_user(
        cls, 
        user_id: str,
        username: str,
        email: str
    ) -> None:
        '''
        update information about this user_id

        Parameters
        ----------
        user_id : str
            Unique user_id
        username : str
        email : str

        Returns
        -------
        None
        '''
        if search_document(
            database_type='user',
            username=username,
            check_response=False
        ):
            raise ValueError('Please use a different username.')
        if search_document(
            database_type='user',
            email=email,
            check_response=False
        ):
            raise ValueError('Please use a different email address.')

        update_document(
            database_type='user',

        )

        token_user_id = get_user_id_from_token()
        if if_token_user_id_equals_user_id(
            token_user_id=token_user_id,
            user_id=user_id
        ):
            current_user_information = g.current_user
            # delete ObjectID to jsonify
            del current_user_information['_id']
            response = {
                'user': current_user_information
            }
            return jsonify(response)
        else:
            raise 'WrongUserId' 
    
    @classmethod
    def comfirm_email(
        cls, token: str
    ) -> bool:

        '''
        A comfirmation link would be sent to user's email.
        User needs to comfirm the email

        Parameters
        ----------
        token : str
            Unique str

        Returns
        -------
        bool
        '''

        is_token_matched(token)
        email = decode_token(token)
        user_document = search_document(
            database_type='user',
            email=email,
            check_response=False
        )

        msg = ''
        if user_document:
            if user_document['confirm_email'] == False:
                if user_document['email'] == email:
                    update_document(
                        database_type='user',
                        confirm_email=True
                    )
                    msg = 'You have confirmed your account. Thanks!'
                else:
                    msg = 'The confirmation link is invalid or has expired.'
            else:
                msg = 'Account already confirmed. Please login.'
        else:
            msg = 'The confirmation link is invalid or has expired.'
        return msg
    
    @classmethod
    def resend_comfirmation_link(
        cls
    ) -> bool:
        '''
        Resend the comfirmation link to user's email

        Parameters
        ----------
        token : str
            Unique str

        Returns
        -------
        bool
        '''
        user_document = search_document(
            database_type='user'
        )
        email = user_document['email']

        token = generate_confirmation_token(email)
        
        confirm_url = url_for(
            'user.confirm_email', 
            token=token, 
            _external=True
        )
        html_template = render_template('activate.html', confirm_url=confirm_url)
        message = "Please confirm your email"
        send_email(
            target_email=email, 
            message=message, 
            html_template=html_template
        )

        return {
            'message': 'Resend successfully!'
        }
    
    @classmethod
    def forgot_pwd(
        cls, 
        username: str,
        email: str
    ) -> dict:
        '''
        Reset the password

        Parameters
        ----------
        username : str
            username
        email : str
            email

        Returns
        -------
        dict
        '''
        user_document = search_document(
            database_type='user'
        )

        if not user_document:
            raise ValueError('Please type in the correct username.')
        if user_document['email'] != email:
            raise ValueError('Please type in the correct username and email.')

        token = generate_confirmation_token(email)
        reset_url = url_for('user.forgot_new', token=token, _external=True)
        html_template = render_template(
            'reset.html',
            username=username,
            reset_url=reset_url
        )
        message = "Reset your password"
        send_email(
            target_email=email, 
            message=message, 
            html_template=html_template
        )

        return {
            'message': 'A password reset email has been sent via email.'
        }
    
    @classmethod
    def update_new_pwd(
        cls, 
        token: str,
    ) -> dict:
        '''
        Update the new password

        Parameters
        ----------
        token : str
            token

        Returns
        -------
        str
        '''
        if not if_token_matched(token):
            flash('Token has expired')
            return 'Token has expired'

        email = decode_token(token)

        user_document = search_document(
            database_type='user',
            email=email
        )
        if not user_document:
            flash('Cannot Find the User according to email')
            return 'Cannot Find the User according to email'
        
        if request.method == 'POST':
    
            password = request.form['newPassword']

            validate_password_indicator, return_message = validate_password(password)
            if not validate_password_indicator:
                msg = ('New password must follow the following instructions: \n'
                    + 'At least 8 characters. At most 25 characters\n'
                    + 'A mixture of both uppercase and lowercase letters\n'
                    + 'A mixture of letters and numbers' 
                    + 'Inclusion of at least one special character, e.g., ! @'
                )
                confirm_url = url_for(
                    'user.forgot_new', 
                    token=token, 
                    msg=msg, 
                    _external=True
                )
                return render_template('forgot_new.html', confirm_url=confirm_url)

            hashed_password = get_hashed_password(password)
            update_document(
                database_type='user',
                email=email,
                hashed_password=hashed_password
            )

            flash('Password successfully changed.')
            return 'Password successfully changed.'
        else:
            msg = 'Hello ' + user_document['username']
            confirm_url = url_for('user.forgot_new', token=token, _external=True)
            return render_template(
                'forgot_new.html', 
                confirm_url=confirm_url, 
                msg=msg, 
                token=token
            )