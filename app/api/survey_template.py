from __future__ import annotations

from app.api import api_bp

from flask import request

from app.error import bad_request

from app.process.api import SurveyTemplate

from app.authentication.api import token_auth

from app.api.utils import handle_response


@api_bp.route('/create_survey_template', methods=['POST'])
@token_auth.login_required
@handle_response
def create_survey_template() -> None:
    '''
    data got from json is dict[dict[str, ]], which has
    3 keys in data: topic name, topic category, topic range
    '''
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'survey_update_method' not in data or not data.get('survey_update_method'):
        return bad_request('survey_update_method is required.') 
    if 'time_period' not in data or not data.get('time_period'):
        return bad_request('time_period is required.') 
    if 'number_of_copies' not in data or not data.get('number_of_copies'):
        return bad_request('number_of_copies is required.')
    if 'max_rounds' not in data or not data.get('max_rounds'):
        return bad_request('max_rounds is required.') 
    if 'survey_topics' not in data or not data.get('survey_topics'):
        return bad_request('survey_topics is required.')
    
    survey_update_method = data['survey_update_method']
    time_period = data['time_period']
    number_of_copies = data['number_of_copies']
    max_rounds = data['max_rounds']
    survey_topics = data['survey_topics']

    return SurveyTemplate.create_survey_template(
        survey_update_method=survey_update_method,
        time_period=time_period,
        number_of_copies=number_of_copies,
        max_rounds=max_rounds,
        survey_topics=survey_topics
    )