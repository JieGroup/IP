from app.process.utils import (
    get_unique_id,
    get_hashed_password
)
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