from __future__ import annotations

from app.api import api

from flask import request

from app.authentication.api import token_auth

from app.utils.api import (
    handle_response,
    Time
)

from app.api.utils import check_if_data_is_valid

from app.database.api import (
    search_document,
    delete_document,
    delete_multiple_documents
)
    
from app.utils.api import Constant

from app.process.api import (
    get_survey_template_helper,
    get_default_survey_template_helper,
    get_user_histories_helper,
    get_voter_answers
)

@api.route('/ceshiyixia', methods=['GET', 'POST'])
@handle_response
def ceshiyixia() -> None:
    '''
    Get all details about default survey template.
    Default survey template is carefully designed by Professor Jie Ding

    Parameters
    ----------
    None

    Returns
    -------
    dict
        Details will be formed in dictonary structure
    '''
    raise ValueError('ceshi')
    return 'ceshiyixia'

@api.route('/get_survey_template', methods=['POST'])
@token_auth.login_required
@handle_response
def get_survey_template() -> dict:
    '''
    Get all details about specific survey template

    Parameters
    ----------
    survey_template_id : str
        An unique string corresponding to a survey template.

    Returns
    -------
    dict
        Details will be formed in dictonary structure
    '''
    data = request.get_json()
    if not data:
        raise ValueError('You must post JSON data.')
    expected_data = {
        'survey_template_id': str,
    }
    check_if_data_is_valid(
        data=data,
        expected_data=expected_data
    )

    survey_template_id = data['survey_template_id']
    survey_template_document = search_document(
        database_type='survey_template',
        survey_template_id=survey_template_id
    )
    del survey_template_document['_id']
    return {
        'survey_template_document': survey_template_document
    }


@api.route('/get_default_survey_template', methods=['GET'])
@handle_response
def get_default_survey_template() -> None:
    '''
    Get all details about default survey template.
    Default survey template is carefully designed by Professor Jie Ding

    Parameters
    ----------
    None

    Returns
    -------
    dict
        Details will be formed in dictonary structure
    '''
    return Constant.generate_default_template()


@api.route('/get_user_histories', methods=['POST'])
@token_auth.login_required
@handle_response
def get_user_histories() -> list:
    '''
    Get all survey templates created by current user

    Parameters
    ----------
    None

    Returns
    -------
    list
        History will be formed in list structure, which sort in 
        reverse timestamp order. (The latest record is in the first place) 
    '''
    # data = request.get_json()
    # if not data:
    #     raise ValueError('You must post JSON data.')
    # expected_data = {
    #     'survey_template_id': str,
    # }
    # check_if_data_is_valid(
    #     data=data,
    #     expected_data=expected_data
    # )

    # survey_template_id = request.args['survey_template_id']
    return get_user_histories_helper()

@api.route('/get_voter_answers_of_template', methods=['POST'])
@token_auth.login_required
@handle_response
def get_voter_answers_of_template() -> list:
    '''
    1. Check if the survey template document and all survey
        answers of current template needs to be deleted.
    2. if the template is not expired, get all survey 
        answers of a specific survey template.

    Parameters
    ----------
    None

    Returns
    -------
    list
        History will be formed in list structure
    '''
    data = request.get_json()
    if not data:
        raise ValueError('You must post JSON data.')
    expected_data = {
        'survey_template_id': str,
    }
    check_if_data_is_valid(
        data=data,
        expected_data=expected_data
    )
    print('data_get_voter_answers_of_template', data)
    survey_template_id = data['survey_template_id']

    survey_template_document = search_document(
        database_type='survey_template',
        survey_template_id=survey_template_id,
        check_response=False
    )
    print('get_voter_answers_of_template', survey_template_document)
    expiration_time = survey_template_document['expiration_time']

    # If the survey template is expired,
    # delete corresponding documents
    if Time.has_expiration_time_expired(
        expiration_time=expiration_time
    ):
        # delete survey_template document
        delete_document(
            database_type='survey_template',
            survey_template_id=survey_template_id
        )

        # delete all survey_answer documents
        delete_multiple_documents(
            database_type='survey_answer',
            survey_template_id=survey_template_id
        )

    return get_voter_answers(
        survey_template_id=survey_template_id
    )