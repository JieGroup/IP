from itertools import count
import sys
import string
import random
import numpy as np

from random import Random
from datetime import datetime, timezone

from app.api import api_bp
from app.utils import Constant
from flask.json import jsonify

from flask import render_template, flash, redirect, url_for, request, session, make_response

from app.error import bad_request

from app.process.api import VoterAnswerSurvey


@api_bp.route('/voter_start_answering', methods=['GET'])
def voter_start_answering():

    '''
    data got from json is dict[dict[str, ]], which has
    3 keys in data: topic name, topic category, topic range
    '''

    data = request.get_json()
    # if not data:
    #     return bad_request('You must post JSON data.')
    # if 'survey_topics' not in data or not data.get('survey_topics'):
    #     return bad_request('survey_topics is required.')
    
    survey_template_id = data['survey_template_id']
    mturk_id = data['mturk_id']
    
    VoterAnswerSurvey.start_answering(
        survey_template_id=survey_template_id,
        mturk_id=mturk_id,
    )

    survey_topics = 5
    response = {
        'survey_topics': survey_topics
    }
    return jsonify(response)


@api_bp.route('/voter_submit_answers', methods=['POST'])
def voter_submit_answers():

    '''
    data got from json is dict[dict[str, ]], which has
    3 keys in data: topic name, topic category, topic range
    '''

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'survey_template_id' not in data or not data.get('survey_template_id'):
        return bad_request('survey_template_id is required.')

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



    
