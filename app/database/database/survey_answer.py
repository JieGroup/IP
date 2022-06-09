from __future__ import annotations

from app import pyMongo
from app.database.database.utils import (
    if_file_size_exceed_limit
)

from app.database.database.base import BaseDatabase

from app.database.database.abstract_database import AbstractDatabase

from app.error import SurveyAnswerTooLarge

from app._typing import Survey_Update_Method

from typing import (
    Union,
    Any
)


class SurveyAnswer(AbstractDatabase, BaseDatabase):

    @classmethod
    def get_all_documents_count(cls):
        return pyMongo.db.SurveyAnswer.estimated_document_count()

    @classmethod
    def get_all_documents(cls, **kwargs):
        if 'survey_template_id' in kwargs:
            return pyMongo.db.SurveyAnswer.find({
                'survey_template_id': kwargs['survey_template_id']
            })
        return pyMongo.db.SurveyAnswer.find({})

    @classmethod
    def search_document(cls, **kwargs):
        return pyMongo.db.SurveyAnswer.find_one({
            'survey_answer_id': kwargs['survey_answer_id']
        })

    @classmethod
    def create_document(
        cls, 
        survey_answer_id: str, 
        survey_template_id: str, 
        mturk_id: str, 
    ) -> None:

        '''
            Create Survey_Answer document
        '''

        survey_answer_document = {
            'survey_answer_id': survey_answer_id,
            'survey_template_id': survey_template_id,
            'mturk_id': mturk_id,
            'survey_answers': {},
        }

        if not if_file_size_exceed_limit(file=survey_answer_document):
            raise SurveyAnswerTooLarge

        return pyMongo.db.SurveyAnswer.insert_one(survey_answer_document)

    @classmethod
    def update_document(
        cls, 
        cur_rounds_num: int,
        survey_answer_id: str,
        survey_new_answers: dict[str, Union[str, dict[str, Any]]], 
    ) -> None:

        '''
            Voter can answer dynamic topics in a survey template multiple times.
            We need to store the answers at each round.
        '''

        rounds_key = f'rounds_{cur_rounds_num}'
        return pyMongo.db.SurveyAnswer.update_one({'survey_answer_id': survey_answer_id}, {'$set':{
                f'survey_answers.{rounds_key}': survey_new_answers,
            }})

    @classmethod
    def delete_document(
        cls, survey_answer_id: str
    ) -> None:

        '''
            Delete corresponding record
        '''

        return pyMongo.db.SurveyAnswer.delete_one({'survey_answer_id': survey_answer_id})
