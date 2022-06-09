from __future__ import annotations

from app.api import api_bp

from flask import request

from app.error import bad_request

from app.authentication.api import token_auth

from app.process.api import Summary

from app.api.utils import handle_response


@api_bp.route('/get_all_survey_answers', methods=['GET'])
@token_auth.login_required
@handle_response
def get_all_survey_answers():

    '''
    data got from json is dict[dict[str, ]], which has
    3 keys in data: topic name, topic category, topic range
    '''

    survey_template_id = request.args.get('survey_template_id')

    # 获取data
    return Summary.get_all_survey_answers(
        survey_template_id=survey_template_id
    )



    
