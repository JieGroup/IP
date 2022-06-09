from __future__ import annotations

from app import pyMongo
from app.database.database.utils import (
    if_file_size_exceed_limit
)

from app.database.database.base import BaseDatabase

from app.database.database.abstract_database import AbstractDatabase

from app.utils.api import Serialization

from app.error import SurveyAnswerTooLarge

from datetime import datetime

from typing import Any


class SurveyTemplate(AbstractDatabase, BaseDatabase):

    @classmethod
    def search_document(
        cls, survey_template_id: str
    ) -> None:

        '''
            Search and return corresponding document
        '''

        return pyMongo.db.SurveyTemplate.find_one({'survey_template_id': survey_template_id})

    @classmethod
    def create_document(
        cls, 
        survey_template_id: str, 
        survey_update_method: str,
        expiration_time: type[datetime],
        number_of_copies: int,
        max_rounds: int,
        survey_topics: dict[dict[str, Any]]
    ) -> None:

        '''
            Store new template in db
        '''

        survey_template_document = {
            'survey_template_id': survey_template_id,
            'survey_update_method': survey_update_method,
            'expiration_time': expiration_time,
            'number_of_copies': number_of_copies,
            'max_rounds': max_rounds,
            'survey_topics': survey_topics,
        }
        survey_template_document = Serialization.make_data_serializable(
            data=survey_template_document
        )
        if not if_file_size_exceed_limit(file=survey_template_document):
            raise SurveyAnswerTooLarge

        return pyMongo.db.SurveyTemplate.insert_one(survey_template_document)
    
    @classmethod
    def update_document(
        cls, 
    ) -> None:

        '''
            Currently not needed. User can only create new template once
        '''

        pass
    
    @classmethod
    def delete_document(
        cls, survey_template_id: str
    ) -> None:

        '''
            Delete corresponding record
        '''

        return pyMongo.db.SurveyTemplate.delete_one({'survey_template_id': survey_template_id})