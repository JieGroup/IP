from __future__ import annotations

from app import pyMongo
from app.database.utils import (
    if_file_size_exceed_limit
)

from app.database.database.base import BaseDatabase

from app.database.database.abstract_database import AbstractDatabase

from typing import Any

class SurveyTemplate(AbstractDatabase, BaseDatabase):

    @classmethod
    def search_document(
        cls, survey_template_id: str
    ) -> None:

        return pyMongo.db.SurveyTemplate.find_one({'survey_template_id': survey_template_id})

    @classmethod
    def create_document(
        cls, 
        survey_template_id: str, 
        current_times_of_template: int,
        survey_topic: dict[dict[str, Any]]
    ) -> None:

        '''
        create template
        '''

        survey_template_document = {
            'survey_template_id': survey_template_id,
            'current_times_of_template': current_times_of_template,
            'survey_topic': survey_topic,
        }

        indicator, BSON_file = if_file_size_exceed_limit(file=survey_template_document)
        if indicator:
            raise ValueError('Answer is too large')

        return pyMongo.db.SurveyTemplate.insert_one(survey_template_document)
    
    @classmethod
    def update_document(
        cls, 
        survey_template_id: str, 
        current_times_of_template: int
    ) -> None:

        return pyMongo.db.Voter.update_one({'survey_template_id': survey_template_id}, {'$set':{
                   'current_times_of_template': current_times_of_template
               }})
    
    @classmethod
    def delete_document(
        cls, survey_template_id
    ) -> None:

        return pyMongo.db.SurveyTemplate.delete_one({'survey_template_id': survey_template_id})