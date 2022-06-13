from __future__ import annotations

from app.api import api_bp

from flask import request

from app.error import bad_request

from app.authentication.api import token_auth

from app.process.api import Summary

from app.utils.api import handle_response


@api_bp.route('/get_all_survey_answers', methods=['GET'])
@token_auth.login_required
@handle_response
def get_all_survey_answers():

    '''
    Get all survey answers under a survey template
    Handle http request in this function and call Summary.get_all_survey_answers
    for further processing

    Parameters
    ----------
    survey_template_id : str
        An unique string corresponding to a survey template.

    Returns
    -------
    list[dict]
        All survey answers would be appended in a list and each term is a dict
    '''

    # TODO: Verify user
    survey_template_id = request.args.get('survey_template_id')

    # 获取data
    return Summary.get_all_survey_answers(
        survey_template_id=survey_template_id
    )