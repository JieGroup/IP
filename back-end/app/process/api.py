from __future__ import annotations

import heapq

from flask import g

from app.process.utils import (
    get_unique_id,
    get_hashed_password
)

from app.utils.api import Time

from app.database.api import search_multiple_documents

from app.process.template import SurveyTemplate
from app.process.answer import VoterAnswerSurvey
from app.process.summary import Summary
from app.process.user import User


__all__ = [
    'get_unique_id',
    'get_hashed_password',
    'SurveyTemplate',
    'VoterAnswerSurvey',
    'Summary',
    'User'
]

from app.database.api import (
    search_document,
    create_document,
    update_document
)

def get_survey_template_helper(
    survey_template_id: str
) -> dict:
    '''
    Get all details about specific survey template

    Parameters
    ----------
    survey_template_id : str
        An unique string corresponding to a survey template.

    Returns
    -------
    dict
        Details will be formed in dictonary structure
    '''
    survey_template_document = search_document(
        database_type='survey_template',
        survey_template_id=survey_template_id,
    )
    del survey_template_document['_id']
    return {
        'survey_template_document': survey_template_document
    }

def get_default_survey_template_helper():
    '''
    Implement later
    '''
    return


def get_user_histories_helper() -> dict[str, list]:  
    '''
    get user history of created survey template
        1. get all created survey template from db
        2. sort it by decreasing time
        3. handle return format
        History data form:
        {
            survey_template_name: str
            survey_template_id: str
                unique template id
            creation_time: str
            status: true or false
                true: still not expire
                false: expire
        }

    Parameters
    ----------
    survey_template_id : str
        An unique string corresponding to a survey template.

    Returns
    -------
    dict[str, list]
    '''
    designed_survey_templates = g.current_user['designed_survey_templates']

    histories = []
    for survey_template_id, item in designed_survey_templates.items():
        survey_template_name = item['survey_template_name']
        creation_time = item['creation_time']
        expiration_time = item['expiration_time']

        sub_res = {}
        sub_res['survey_template_name'] = survey_template_name
        sub_res['survey_template_id'] = survey_template_id
        current_time = Time.get_current_utc_time()
        if current_time > expiration_time:
            sub_res['status'] = False
        elif current_time <= expiration_time:
            sub_res['status'] = True
        
        # change creation_time to user friendly string
        sub_res['creation_time'] = Time.change_time_to_readable_str(
            creation_time=creation_time
        )

        heapq.heappush(histories, (-creation_time, sub_res))

    sorted_histories = []
    while histories:
        _, sub_res = heapq.heappop(histories)
        sorted_histories.append(sub_res)

    return {
        'histories': sorted_histories
    }

def get_voter_answers(
    survey_template_id: str
) -> dict[str, list]:
    '''
    get all voter answers of a survey_template_id

    Parameters
    ----------
    survey_template_id : str
        An unique string corresponding to a survey template.

    Returns
    -------
    dict[str, list]
    '''
    multiple_documents = search_multiple_documents(
        database_type='survey_answer',
        survey_template_id=survey_template_id,
        check_response=False
    )

    res = []
    for doc in multiple_documents:
        del doc['_id']
        res.append(doc)
        res.append('\n')
    
    return {
        'voter_answers': res
    }