from app.process.utils import (
    get_unique_id,
    get_hashed_password
)

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
    ) -> None:

        return search_document(
            database_type='survey_template',
            survey_template_id=survey_template_id,
        )

def get_default_survey_template_helper():

    '''
    Implement later
    '''

    return


def get_user_history_helper():  

    '''
    Implement later
    '''

    return

def get_voter_answers(
    survey_template_id: str
) -> list:
    '''
    get all voter answers of a survey_template_id

    Parameters
    ----------
    survey_template_id : str
        An unique string corresponding to a survey template.

    Returns
    -------
    list
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
    
    return res