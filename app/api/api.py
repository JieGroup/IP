from __future__ import annotations

from app.api import api_bp

from flask import request

from app.error import bad_request

from app.authentication.api import token_auth

from app.api.utils import handle_response

from app.process.api import (
    get_survey_template_helper,
    get_default_survey_template_helper,
    get_user_history_helper
)

@api_bp.route('/get_survey_template', methods=['GET'])
@token_auth.login_required
@handle_response
def get_survey_template() -> None:

    '''
    data got from json is dict[dict[str, ]], which has
    3 keys in data: topic name, topic category, topic range
    '''
    # TODO: implement logic
    return get_survey_template_helper()


@api_bp.route('/get_default_survey_template', methods=['GET'])
@handle_response
def get_default_survey_template() -> None:

    '''
    data got from json is dict[dict[str, ]], which has
    3 keys in data: topic name, topic category, topic range
    '''

    return get_default_survey_template_helper()


@api_bp.route('/get_user_history', methods=['GET'])
@token_auth.login_required
@handle_response
def get_user_history() -> None:

    '''
    data got from json is dict[dict[str, ]], which has
    3 keys in data: topic name, topic category, topic range
    '''

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    
    return get_user_history_helper()