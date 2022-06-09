from app.process.template import SurveyTemplate
from app.process.answer import VoterAnswerSurvey
from app.process.summary import Summary

__all__ = [
    'SurveyTemplate',
    'VoterAnswerSurvey',
    'Summary'
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