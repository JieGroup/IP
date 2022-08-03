from __future__ import annotations

from pyparsing import str_type

from app.api import api

from flask import request

from flask.json import jsonify

from app.process.api import SurveyTemplate

from app.authentication.api import token_auth

from app.utils.api import handle_response

from app.api.utils import check_if_data_is_valid

from app._typing import (
    Survey_Update_Method,
    Survey_Topics
)

from typing import Any


@api.route('/create_survey_template', methods=['POST'])
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
    time_period : str
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
    print('template', request)
    data = request.get_json()
    if not data:
        raise ValueError('You must post JSON data.')
    print('zheli', data)
    expected_data = {
        'survey_template_name': str,
        'survey_update_method': Survey_Update_Method,
        'time_period': str,
        'number_of_copies': int,
        'max_rounds': int,
        'survey_topics': Survey_Topics
    }
    check_if_data_is_valid(
        data=data,
        expected_data=expected_data
    )
    print('0.5')
    survey_template_name = data['survey_template_name']
    survey_update_method = data['survey_update_method']
    time_period = data['time_period']
    number_of_copies = data['number_of_copies']
    max_rounds = data['max_rounds']
    survey_topics = data['survey_topics']

    res = SurveyTemplate.create_survey_template(
        survey_template_name=survey_template_name,
        survey_update_method=survey_update_method,
        time_period=time_period,
        number_of_copies=number_of_copies,
        max_rounds=max_rounds,
        survey_topics=survey_topics
    )
    print('create_template', res)

    return res