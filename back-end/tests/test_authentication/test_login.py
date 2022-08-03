import json
import pytest

from tests.conftest import (
    get_test_client,
    get_empty_headers,
    get_basic_auth_headers,
    get_token_auth_headers,
    get_form_type_headers
)

from .utils import (
    get_api_url,
    get_auth_url
)

from app.database.api import search_document

from app.authentication.token_auth import get_voterToken

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

class TestLogin:

    # @pytest.mark.parametrize(
    #     "username, email, password", 
    #     [
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
    #         (   
    #             'username_4',
    #             'IntervalPrivacy@gmail.com',
    #             'Password_2'
    #         ),
    #     ]
    # )
    # def test_user_login(self, username, email, password):
        
    #     client = get_test_client()
    #     headers = get_empty_headers()
    #     register(
    #         client=client,
    #         headers=headers,
    #         username=username,
    #         email=email,
    #         password=password
    #     )

    #     basic_auth_headers = get_basic_auth_headers(
    #         username=username,
    #         password=password
    #     )
    #     response = client.post(
    #         get_auth_url('get_userToken'), 
    #         headers=basic_auth_headers, 
    #     )
    #     assert response.status_code == 200
    #     res = json.loads(response.get_data(as_text=True))
    #     assert 'userToken' in res
    #     assert type(res['userToken']) == str

    @pytest.mark.parametrize(
        "survey_template_id, mturk_id", 
        [
            (   
                'username_4',
                'IntervalPrivacy@gmail.com',
            ),
        ]
    )
    def test_voter_login(self, survey_template_id, mturk_id):
        
        res = get_voterToken(
            survey_template_id=survey_template_id,
            mturk_id=mturk_id
        )
        res = json.loads(res)
        assert 'voterToken' in res
        assert type(res['voterToken']) == str



    # @pytest.mark.usefixtures('DatabaseOperator_instance')
    # @pytest.mark.parametrize("test_record, expected_res", [
    #     (('test', 'test', 'test1'), ''),
    #     (('test', 'test', 'test2'), 'test')
    # ])
    # def test_get_record(self, DatabaseOperator_instance, test_record, expected_res):
    #     response = DatabaseOperator_instance.get_record(
    #         user_id=test_record[0], 
    #         train_id=test_record[1], 
    #         algorithm_data_name=test_record[2],
    #     )
    #     assert response == expected_res