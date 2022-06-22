from __future__ import annotations

from app.api import api

from flask import request

from app.authentication.api import token_auth

from app.utils.api import handle_response

from app.api.utils import check_if_data_is_valid

from app.process.api import (
    get_survey_template_helper,
    get_default_survey_template_helper,
    get_user_history_helper
)

@api.route('/get_survey_template', methods=['GET'])
# @token_auth.login_required
# @handle_response
def get_survey_template() -> None:
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
    expected_data = {
        'survey_template_id': str,
    }
    check_if_data_is_valid(
        data=request.args,
        expected_data=expected_data
    )

    survey_template_id = request.args['survey_template_id']

    # TODO: implement logic
    # res = get_survey_template_helper()
    res = 5
    return res


@api.route('/get_default_survey_template', methods=['GET'])
# @handle_response
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
    return get_default_survey_template_helper()


@api.route('/get_user_history', methods=['GET'])
@token_auth.login_required
# @handle_response
def get_user_history() -> None:
    '''
    Get all survey template created by the current user.

    Parameters
    ----------
    None

    Returns
    -------
    list
        History will be formed in list structure, which sort in 
        reverse timestamp order. (The latest record is in the first place) 
    '''
    expected_data = {
        'user_id': str,
    }
    check_if_data_is_valid(
        data=request.args,
        expected_data=expected_data
    )

    user_id = request.args['user_id']
    
    return get_user_history_helper()