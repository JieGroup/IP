from __future__ import annotations

from app.database.api import get_all_documents

from typeguard import typechecked


@typechecked
class Summary:
    '''
    Handle the summary process - creator gets the information
    about the survey. 

    Attributes
    ----------
    None

    Methods
    -------
    get_all_survey_answers
    '''

    @classmethod
    def get_all_survey_answers(
        cls,
        survey_template_id: str
    ) -> list[dict]:
        '''
        Return all the survey answer documents that are belonged to
        current survey_template_id

        Parameters
        ----------
        survey_template_id : str
            An unique string corresponding to an answer of a survey template.

        Returns
        -------
        list[dict]
        '''
        return get_all_documents(
            database_type='survey_answer',
            survey_template_id=survey_template_id
        )

