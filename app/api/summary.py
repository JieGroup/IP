from itertools import count
import sys
import string
import random
import numpy as np

from random import Random
from datetime import datetime, timezone

from app.api import api_bp
from app.utils import Constant
from app.database import select_mongoDB_operator

from flask import render_template, flash, redirect, url_for, request, session, make_response

from app.error import bad_request

from app.process.api import SurveyTemplate


@api_bp.route('/get_summary', methods=['GET'])
@token_auth.login_required
def get_summary():

    '''
    data got from json is dict[dict[str, ]], which has
    3 keys in data: topic name, topic category, topic range
    '''

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'survey_template_id' not in data or not data.get('survey_template_id'):
        return bad_request('survey_template_id is required.')

    survey_template_id = data['survey_template_id']

    # 获取data
    SurveyTemplate.update_survey_template(
        survey_template_id=survey_template_id,
        root_key=root_key
    )



    
