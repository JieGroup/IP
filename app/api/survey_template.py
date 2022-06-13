from __future__ import annotations

from app.api import api_bp

from flask import request

from app.error import bad_request

from app.process.api import SurveyTemplate

from app.authentication.api import token_auth

from app.utils.api import handle_response

from flask.json import jsonify

@api_bp.route('/ceshierror', methods=['GET', 'POST'])
def ceshierror():

    a = {}
    print('zheli')
    # b = a['5']
    return jsonify('success')


@api_bp.route('/create_survey_template', methods=['POST'])
@token_auth.login_required
@handle_response
def create_survey_template() -> None:

    '''
    Create survey template
    Handle http request in this function and call SurveyTemplate.create_survey_template
    for further processing

    Parameters
    ----------
    survey_update_method : Survey_Update_Method
        Defines how we update topic new ranges. 'static' means the voter would only answer
        the all topics once. 'uniform' means the topics would be dynamically generated and voter
        may need to answer each topic more than one time.
    time_period : int
        Defines how long we should keep the survey template in database
    number_of_copies : int
        Defines the max number of survey to issue
    max_rounds : int
        Defines how many times the topic can be regenerated
    survey_topics : dict
        The detailed information of each topic

    Returns
    -------
    str
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