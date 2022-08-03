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
    generate_email_confirmation_token,
    send_email,
    get_user_id_from_token,
    if_token_user_id_equals_user_id,
    check_if_email_token_matched,
    decode_email_token
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
    ) -> dict:
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
        dict
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
            designed_survey_template={}
        )
        
        token = generate_email_confirmation_token(
            username=username,
            email=email
        )
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
        return {
            'token': token
        }

    @classmethod
    def resend_email_confirmation_link(
        cls,
        username: str,
        email: str
    ) -> dict:
        '''
        Resend the confirmation link to user's email

        Parameters
        ----------
        username : str
            Unique str
        email : str

        Returns
        -------
        dict
        '''
        token = generate_email_confirmation_token(
            username=username,
            email=email
        )
        
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
        return {
            'token': token
        }
    
    @classmethod
    def confirm_email(
        cls, token: str
    ) -> str:
        '''
        A confirmation link would be sent to user's email.
        User needs to confirm the email

        Parameters
        ----------
        token : str
            Unique str

        Returns
        -------
        str
        '''
        check_if_email_token_matched(token)
        decoded_token = decode_email_token(token)
        username = decoded_token['username']
        email = decoded_token['email']
        user_document = search_document(
            database_type='user',
            username=username,
            check_response=False
        )
        user_id = user_document['user_id']

        msg = ''
        if user_document:
            if user_document['confirm_email'] == False:
                if user_document['email'] == email:
                    update_document(
                        database_type='user',
                        user_id=user_id,
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
    def get_own_info(
        cls
    ) -> dict:
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
        current_user_information = g.current_user
        # delete ObjectID to jsonify
        del current_user_information['_id']
        return {
            'user_document': current_user_information
        }
    
    @classmethod
    def reset_pwd(
        cls, 
        username: str,
        email: str,
        password: str,
    ) -> dict:
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
        user_document = search_document(
            database_type='user',
            username=username
        )

        if not user_document:
            raise ValueError('Please type in the correct username.')
        if user_document['email'] != email:
            raise ValueError('Please type in the correct username and email.')

        token = generate_email_confirmation_token(
            username=username,
            email=email
        )
        
        reset_url = url_for(
            'api.update_new_pwd', 
            token=token, 
            _external=True
        )
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
            'token': token
        }
    
    @classmethod
    def update_new_pwd(
        cls, 
        token: str,
        request: object,
    ) -> Any:
        '''
        Update the new password

        Parameters
        ----------
        token : str
            token
        request : object
            request from front-end

        Returns
        -------
        Any
        '''
        if not check_if_email_token_matched(token):
            flash('Token has expired')
            return 'Token has expired'

        decoded_token = decode_email_token(token)
        username = decoded_token['username']
        email = decoded_token['email']
        user_document = search_document(
            database_type='user',
            username=username
        )
        if not user_document:
            flash('Cannot Find the User according to email')
            return 'Cannot Find the User according to email'
        
        if request.method == 'POST':
            password = request.form['newPassword']
            validate_password_indicator, return_message = validate_password(password)
            if not validate_password_indicator:
                msg = ('New password must follow the following instructions: \n'
                    + 'At least 8 characters. At most 40 characters\n'
                    + 'A mixture of both uppercase and lowercase letters\n'
                    + 'A mixture of letters and numbers!' 
                )
                confirm_url = url_for(
                    'api.update_new_pwd', 
                    token=token, 
                    msg=msg, 
                    _external=True
                )
                return render_template('forgot_new.html', confirm_url=confirm_url)
            user_id = user_document['user_id']
            hashed_password = get_hashed_password(password)
            update_document(
                database_type='user',
                user_id=user_id,
                hashed_password=hashed_password
            )

            flash('Password successfully changed.')
            return 'Password successfully changed.'
        else:
            msg = 'Hello ' + user_document['username']
            confirm_url = url_for(
                'api.update_new_pwd', 
                token=token, 
                _external=True
            )
            return render_template(
                'forgot_new.html', 
                confirm_url=confirm_url, 
                msg=msg, 
                token=token
            )


    

    # @classmethod
    # def update_user(
    #     cls, 
    #     user_id: str,
    #     username: str,
    #     email: str
    # ) -> None:
    #     '''
    #     update information about this user_id

    #     Parameters
    #     ----------
    #     user_id : str
    #         Unique user_id
    #     username : str
    #     email : str

    #     Returns
    #     -------
    #     None
    #     '''
    #     if search_document(
    #         database_type='user',
    #         username=username,
    #         check_response=False
    #     ):
    #         raise ValueError('Please use a different username.')
    #     if search_document(
    #         database_type='user',
    #         email=email,
    #         check_response=False
    #     ):
    #         raise ValueError('Please use a different email address.')

    #     update_document(
    #         database_type='user',

    #     )

    #     token_user_id = get_user_id_from_token()
    #     if if_token_user_id_equals_user_id(
    #         token_user_id=token_user_id,
    #         user_id=user_id
    #     ):
    #         current_user_information = g.current_user
    #         # delete ObjectID to jsonify
    #         del current_user_information['_id']
    #         response = {
    #             'user': current_user_information
    #         }
    #         return jsonify(response)
    #     else:
    #         raise 'WrongUserId' 