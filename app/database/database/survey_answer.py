from __future__ import annotations

from app import pyMongo
from app.database.utils import (
    if_file_size_exceed_limit
)

from app.database.database.base import BaseDatabase

from app.database.database.abstract_database import AbstractDatabase

from app._typing import Survey_Update_Method

from typing import (
    Union,
    Any
)


class SurveyAnswer(AbstractDatabase, BaseDatabase):

    @classmethod
    def get_all_documents_count(cls, **kwargs):
        if 'survey_update_method' in kwargs:
            return pyMongo.db.SurveyAnswer.count_documents({'survey_update_method': kwargs['survey_update_method']})
        else:
            # print(dir(pyMongo.db.SurveyAnswer))
            return pyMongo.db.SurveyAnswer.estimated_document_count()

    @classmethod
    def get_all_documents(cls, **kwargs):
        if 'mturk_id' in kwargs and 'survey_update_method' in kwargs:
            return pyMongo.db.SurveyAnswer.find({'mturk_id': kwargs['mturk_id'], 'survey_update_method': kwargs['survey_update_method']})
        else:
            return pyMongo.db.SurveyAnswer.find({})

    @classmethod
    def search_document(cls, **kwargs):
        if 'survey_answer_id' in kwargs:
            return pyMongo.db.SurveyAnswer.find_one({'survey_answer_id': kwargs['survey_answer_id']})
        elif 'token' in kwargs:
            return pyMongo.db.SurveyAnswer.find_one({'token': kwargs['token']})
        else:
            raise ValueError('Please input correct SurveyAnswer key')


    @classmethod
    def create_document(
        cls, 
        survey_answer_id: str, 
        survey_template_id: str, 
        mturk_id: str, 
        current_times_of_template: int,
        survey_update_method: Survey_Update_Method, 
        token: str,
    ) -> None:

        # calculate survey_round
        # prev_survey_round = pyMongo.db.SurveyAnswer.count_documents({
        #     'survey_template_id': survey_template_id, 
        #     'mturk_id': mturk_id
        # })

        # print(f'prev_survey_round: {prev_survey_round}')
        # survey_round = prev_survey_round + 1
        survey_answer_document = {
            'survey_answer_id': survey_answer_id,
            'survey_template_id': survey_template_id,
            'mturk_id': mturk_id,
            'current_times_of_template': current_times_of_template,
            'survey_update_method': survey_update_method,
            'token': token,
            'survey_answers': {},
        }

        indicator, BSON_file = if_file_size_exceed_limit(file=survey_answer_document)
        if indicator:
            raise ValueError('Answer is too large')

        return pyMongo.db.SurveyAnswer.insert_one(survey_answer_document)
    
    @classmethod
    def get_current_round(
        cls, survey_answer_id: str
    ) -> int:

        survey_answer_document = cls.search_document(survey_answer_id=survey_answer_id)
        cur_round = len(survey_answer_document['survey_answers']) + 1

        return cur_round

    @classmethod
    def update_document(
        cls, 
        token: str, 
        survey_answer_id: str,
        # survey_topic: str, 
        survey_answers: dict[str, Union[str, dict[str, Any]]], 
        start_time: str, 
        end_time: str, 
        # answer_type: str
    ) -> None:

        # if survey_topic == 'MTurk':
        #     return pyMongo.db.SurveyAnswer.update_one({'token': token}, {'$set':{
        #             'mturk_id': survey_answer,
        #         }})
        # else:
        cur_round = cls.get_current_round(survey_answer_id=survey_answer_id)
        rounds_key = 'rounds_' + str(cur_round)
        # print('lihai{survey_answer_document}+{cur_round}')
        return pyMongo.db.SurveyAnswer.update_one({'token': token}, {'$set':{
                f'survey_answers.{rounds_key}': survey_answers,
            }})

    @classmethod
    def delete_document(
        cls, survey_answer_id: str
    ) -> None:

        return pyMongo.db.SurveyAnswer.delete_one({'survey_answer_id': survey_answer_id})
