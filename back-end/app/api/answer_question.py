from __future__ import annotations

from app.api import api

from flask import request

from flask import abort

from app.authentication.api import token_auth

from app.process.api import VoterAnswerSurvey

from app.utils.api import handle_response

from app.api.utils import check_if_data_is_valid

from typing import Any

from app._typing import (
    MTurkID,
    Survey_New_Answers
)


@api.route('/voter_start_answering', methods=['POST'])
@handle_response
def voter_start_answering():

    '''
    Voter upload parameters to get survey template.
    Handle http request in this function and call VoterAnswerSurvey.start_answering
    for further processing

    Parameters
    ----------
    survey_template_id : str
        An unique string corresponding to a survey template.
    mturk_id : MTurkID
        Defines how long we should keep the survey template in database

    Returns
    -------
    dict
    '''
    # raise ValueError
    # abort(401)
    data = request.get_json()
    if not data:
        raise ValueError('You must post JSON data.')
    expected_data = {
        'survey_template_id': str,
        'mturk_id': MTurkID
    }
    check_if_data_is_valid(
        data=data,
        expected_data=expected_data
    )

    survey_template_id = data['survey_template_id']
    mturk_id = data['mturk_id']
    return VoterAnswerSurvey.start_answering(
        survey_template_id=survey_template_id,
        mturk_id=mturk_id,
    )


@api.route('/voter_submit_answers', methods=['POST'])
@token_auth.login_required
@handle_response
def voter_submit_answers():
    '''
    Voter upload parameters and new answers for a survey template.
    Handle http request in this function and call VoterAnswerSurvey.update_survey_topics
    for further processing

    Parameters
    ----------
    survey_answer_id : str
        An unique string corresponding to an answer of a survey template.
    survey_new_answers : Survey_New_Answers
        New answers

    Returns
    -------
    None or dict
        If the voter has finished all rounds of survey, return None.
        Otherwise return new topics
    '''
    data = request.get_json()
    if not data:
        raise ValueError('You must post JSON data.')
    print(f'voter_submit_answers: {data}')
    expected_data = {
        'survey_answer_id': str,
        'survey_new_answers': Survey_New_Answers,
    }
    check_if_data_is_valid(
        data=data,
        expected_data=expected_data,
    )

    survey_answer_id = data['survey_answer_id']
    survey_new_answers = data['survey_new_answers']
    print('???survey_new_answers', survey_new_answers, len(survey_new_answers))
    if len(survey_new_answers) == 0:
        raise ValueError('cannot input empty survey_new_answers')
    print('1')
    return VoterAnswerSurvey.update_survey_topics(
        survey_answer_id=survey_answer_id,
        survey_new_answers=survey_new_answers,
    )