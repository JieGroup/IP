from __future__ import annotations

import json
import pytest
import requests
from app.database.api import search_document

from tests.conftest import (
    get_empty_headers,
    get_test_client,
    get_token_auth_headers,
    get_form_type_headers
)

from .utils import (
    get_api_url,
    select_first_option,
    stop_first_topic
)

from app.utils.api import Constant

from app.process.api import (
    SurveyTemplate,
    VoterAnswerSurvey
)

from app.error import DBDocumentNotFound


def register(
    client,
    headers,
    username,
    email,
    password,
) -> dict:
    '''
    Notes
    -----
    Include create_user and confirm_email
    '''
    data = json.dumps({
        'username': username,
        'email': email,
        'password': password,
    })
    response = client.post(
        get_api_url('create_user'), 
        headers=headers, 
        data=data
    )
    assert response.status_code == 200
    email_token = json.loads(response.get_data(as_text=True))['token']

    response = client.get(
        get_api_url('confirm_email') + f'/{email_token}'
    )
    user_document = search_document(
        database_type='user',
        username=username
    )
    assert user_document['username'] == username
    assert user_document['confirm_email'] == True



class TestUser():

    @pytest.mark.parametrize(
        "username, email, password", 
        [
            # (   
            #     'username_1',
            #     'email_1@123.com',
            #     'Password_1'
            # ),
            # (   
            #     'username_2',
            #     'email_2@123.com',
            #     'Password_2'
            # ),
            # (   
            #     'username_3',
            #     'IntervalPrivacy@gmail.com',
            #     'Password_2'
            # ),
            (   
                'username_4',
                'IntervalPrivacy@gmail.com',
                'Password_2'
            ),
        ]
    )
    def test_register(self, username, email, password):
        
        client = get_test_client()
        headers = get_empty_headers()
        register(
            client=client,
            headers=headers,
            username=username,
            email=email,
            password=password
        )


    @pytest.mark.parametrize(
        "username, email, password", 
        [
            # (   
            #     'username_1',
            #     'email_1@123.com',
            #     'Password_1'
            # ),
            # (   
            #     'username_2',
            #     'email_2@123.com',
            #     'Password_2'
            # ),
            # (   
            #     'username_3',
            #     'IntervalPrivacy@gmail.com',
            #     'Password_2'
            # ),
            (   
                'username_4',
                'IntervalPrivacy@gmail.com',
                'Password_2'
            ),
        ]
    )
    def test_resend_email_confirmation_link(self, username, email, password):
        
        client = get_test_client()
        headers = get_empty_headers()
        data = json.dumps({
            'username': username,
            'email': email,
            'password': password,
        })
        response = client.post(
            get_api_url('create_user'), 
            headers=headers, 
            data=data
        )
        assert response.status_code == 200

        data = json.dumps({
            'username': username,
            'email': email,
        })
        response = client.post(
            get_api_url('resend_email_confirmation_link'), 
            headers=headers, 
            data=data
        )
        assert response.status_code == 200
        email_token = json.loads(response.get_data(as_text=True))['token']

        response = client.get(
            get_api_url('confirm_email') + f'/{email_token}'
        )
        user_document = search_document(
            database_type='user',
            username=username
        )
        assert user_document['username'] == username
        assert user_document['confirm_email'] == True

    @pytest.mark.parametrize(
        "username, email, password", 
        [
            (   
                'username_1',
                'email_1@123.com',
                'Password_1'
            ),
            (   
                'username_2',
                'email_2@123.com',
                'Password_2'
            ),
            (   
                'username_3',
                'IntervalPrivacy@gmail.com',
                'Password_2'
            ),
            (   
                'username_4',
                'IntervalPrivacy@gmail.com',
                'Password_2'
            ),
        ]
    )
    def test_reset_pwd(self, username, email, password):
        
        client = get_test_client()
        headers = get_empty_headers()
        register(
            client=client,
            headers=headers,
            username=username,
            email=email,
            password=password
        )
        
        password = 'Asdfasdfsadfsf1'
        data = json.dumps({
            'username': username,
            'email': email,
            'password': password
        })
        response = client.post(
            get_api_url('reset_pwd'), 
            headers=headers, 
            data=data
        )
        assert response.status_code == 200
        email_token = json.loads(response.get_data(as_text=True))['token']

        response = client.get(
            get_api_url('update_new_pwd') + f'/{email_token}', 
        )
        assert response.status_code == 200
        
        print('!----------')
        data = {
            'newPassword': 'N1ewnewnew',
            'token': email_token
        }
        headers = get_form_type_headers()
        response = client.post(
            get_api_url('update_new_pwd') + f'/{email_token}',
            headers=headers,
            data=data
        )
        assert response.status_code == 200
        res = json.loads(response.get_data(as_text=True))
        assert res == 'Password successfully changed.'

