from __future__ import annotations

from app.api import api_bp

from flask import request

from app.authentication.api import token_auth

from app.error import bad_request

from app.process.api import VoterAnswerSurvey

from app.utils.api import handle_response

from app._typing import MTurkID


@api_bp.route('/voter_start_answering', methods=['GET'])
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

    survey_template_id = request.args.get('survey_template_id')
    mturk_id = request.args.get('mturk_id')

    if survey_template_id is None:
        return bad_request('survey_answer_id is required.')
    if mturk_id is None:
        return bad_request('mturk_id is required.')
    
    return VoterAnswerSurvey.start_answering(
        survey_template_id=survey_template_id,
        mturk_id=mturk_id,
    )


@api_bp.route('/voter_submit_answers', methods=['POST'])
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
    survey_new_answers : dict[dict[str, Any]]
        New answers

    Returns
    -------
    None or dict
        If the voter has finished all rounds of survey, return None.
        Otherwise return new topics
    '''

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'survey_answer_id' not in data or not data.get('survey_answer_id'):
        return bad_request('survey_answer_id is required.')
    if 'survey_new_answers' not in data or not data.get('survey_new_answers'):
        return bad_request('survey_new_answers is required.')

    survey_answer_id = data['survey_answer_id']
    survey_new_answers = data['survey_new_answers']
    start_time = data['start_time']
    end_time = data['end_time']
    
    return VoterAnswerSurvey.update_survey_topics(
        survey_answer_id=survey_answer_id,
        survey_new_answers=survey_new_answers,
        start_time=start_time,
        end_time=end_time
    )