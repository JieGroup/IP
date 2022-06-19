from __future__ import annotations

import json
import unittest

from base64 import b64encode

from tests import TestConfig

from bson import ObjectId

from app import (
    create_app, 
    pyMongo
)

from app.database.api import (
    search_document,
    create_document,
    update_document
)

from app.process.api import (
    get_hashed_password,
    get_unique_id
)


'''
1. Handle the funcions applied before each test and after each test.
2. Contain some common functions
'''


app = None
app_context = None
client = None
def pytest_runtest_setup() -> None:
    '''
    Execute before every test
    Create test flask client

    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    print('---- pytest_runtest_setup')
    global app, app_context, client
    app = create_app(TestConfig)
    # active context of flask instance  
    app_context = app.app_context()
    app_context.push()
    # Flask's built-in test client that simulates browser behavior
    # to interact with server
    client = app.test_client()

def pytest_runtest_teardown() -> None:

    '''
    Execute after every test
    Clean database and exit the flask instance context

    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    print('---- pytest_runtest_teardown')
    global app_context
    drop_db_collections()
    app_context.pop()

def get_test_client() -> object:
    global client
    return client

def drop_db_collections() -> None:
        
    '''
    Clean database

    Parameters
    ----------
    None

    Returns
    -------
    None
    '''

    for collecion_names in pyMongo.db.list_collection_names():
        pyMongo.db.drop_collection(collecion_names)

def get_basic_auth_headers(
    username: str, 
    password: str
) -> dict:

    '''
    Create headers for the Basic Auth

    Parameters
    ----------
    None

    Returns
    -------
    dict
    '''

    return {
        'Authorization': 'Basic ' + b64encode(
            (username + ':' + password).encode('utf-8')).decode('utf-8'),
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def get_token_auth_headers(
    username: str, 
    password: str
) -> dict:

    '''
    Create headers for the JSON Web Token

    Parameters
    ----------
    None

    Returns
    -------
    dict
    '''

    global client

    headers = get_basic_auth_headers(
        username=username, 
        password=password
    )
    response = client.post('/auth/tokens', headers=headers)
    assert response.status_code == 200
    json_response = json.loads(response.get_data(as_text=True))
    assert json_response is not None
    token = json_response['token']
    return {
        'Authorization': 'Bearer ' + token,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def register_account(
    username: str
) -> str:

    '''
    Create account for further testing.
    If the document containing the username already exists,
    return the existing document

    Parameters
    ----------
    username : str
        username must be unique in db

    Returns
    -------
    str
    '''

    user_document = search_document(
        database_type='user',
        username=username
    )

    user_id = None
    if user_document == None:
        user_id = get_unique_id()
        hashed_password = get_hashed_password('Xie1@456')
    
        create_document(
            database_type='user',
            user_id=user_id,
            username=username,
            hashed_password=hashed_password,
            comfirm_email=True
        )
    else:
        user_id = user_document['user_id']

    return user_id

def get_two_accounts() -> tuple[str, str]:

    '''
    Get 2 accounts for further testing

    Parameters
    ----------
    None

    Returns
    -------
    tuple[str, str]
    '''

    user_id_1 = register_account(
        username='unittest1'
    )

    user_id_2 = register_account(
        username='unittest2'
    )

    return (user_id_1, user_id_2)