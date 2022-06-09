from __future__ import annotations

from app import pyMongo
from app.database.database.utils import (
    if_file_size_exceed_limit
)

from app.database.database.base import BaseDatabase

from app.database.database.abstract_database import AbstractDatabase

from typing import Any


class SurveySummary(AbstractDatabase, BaseDatabase):

    @classmethod
    def search_document(
        cls, identifier_id: str
    ) -> None:

        return pyMongo.db.SurveySummary.find_one({'identifier_id': identifier_id})

    @classmethod
    def create_document(
        cls, survey_template_id: str, 
    ) -> None:

        survey_summary_document = {
            'survey_template_id': survey_template_id,
            'survey_topic': {},
        }

        indicator, BSON_file = if_file_size_exceed_limit(file=survey_summary_document)
        if indicator:
            raise ValueError('Answer is too large')

        return pyMongo.db.SurveySummary.insert_one(survey_summary_document)
    
    @classmethod
    def update_document(
        cls, 
        survey_template_id: str, 
        survey_topic: dict[dict[str, Any]]
    ) -> None:

        return pyMongo.db.SurveySummary.update_one({'survey_template_id': survey_template_id}, {'$set':{
                   'survey_topic': survey_topic
               }})
    
    @classmethod
    def delete_document(
        cls, survey_template_id: str
    ) -> None:

        return pyMongo.db.SurveySummary.delete_one({'survey_template_id': survey_template_id})