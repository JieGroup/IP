from __future__ import annotations

from app.api import api

from flask import request

from app.error import bad_request

from app.authentication.api import token_auth

from app.utils.api import handle_response

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

    survey_template_id = request.args.get('survey_template_id')

    if survey_template_id is None:
        return bad_request('survey_answer_id is required.')

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

    user_id = request.args.get('user_id')

    if user_id is None:
        return bad_request('user_id is required.')
    
    return get_user_history_helper()