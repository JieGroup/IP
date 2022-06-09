from __future__ import annotations
from app.api import survey_template
from app.error import bad_request

from bson import ObjectId

from app.utils.api import obtain_unique_id

from typing import Any

from app.database.api import (
    search_document,
    create_document,
    update_document
)

from app.utils.api import Time

from app.utils.constant import Constant

from app._typing import Survey_Update_Method


class Summary:

    '''
    Handle the summary process.

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
        survey_update_method : str

        Returns
        -------
        list[dict]
        '''

        return search_document(
            database_type='survey_answer',
            survey_template_id=survey_template_id
        )

