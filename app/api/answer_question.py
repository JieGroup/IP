from __future__ import annotations

from app.api import api_bp

from flask import request

from app.authentication.api import token_auth

from app.error import bad_request

from app.process.api import VoterAnswerSurvey

from app.api.utils import handle_response


@api_bp.route('/voter_start_answering', methods=['GET'])
@handle_response
def voter_start_answering():

    '''
    data got from json is dict[dict[str, ]], which has
    3 keys in data: topic name, topic category, topic range
    '''

    survey_template_id = request.args.get('survey_template_id')
    mturk_id = request.args.get('mturk_id')
    
    return VoterAnswerSurvey.start_answering(
        survey_template_id=survey_template_id,
        mturk_id=mturk_id,
    )


@api_bp.route('/voter_submit_answers', methods=['POST'])
@handle_response
def voter_submit_answers():

    '''
    data got from json is dict[dict[str, ]], which has
    3 keys in data: topic name, topic category, topic range
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