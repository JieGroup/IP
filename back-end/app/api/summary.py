from __future__ import annotations

from app.api import api

from flask import request

from app.authentication.api import token_auth

from app.process.api import Summary

from app.utils.api import handle_response

from app.api.utils import check_if_data_is_valid


@api.route('/get_all_survey_answers', methods=['GET'])
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
    expected_data = {
        'survey_template_id': str,
    }
    check_if_data_is_valid(
        data=request.args,
        expected_data=expected_data
    )
    # TODO: Verify user
    survey_template_id = request.args['survey_template_id']

    # 获取data
    return Summary.get_all_survey_answers(
        survey_template_id=survey_template_id
    )