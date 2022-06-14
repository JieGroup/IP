from __future__ import annotations

from app import pyMongo
from app.database.database.utils import (
    if_file_size_exceed_limit
)

from app.database.database.base import BaseDatabase

from app.database.database.abstract_database import AbstractDatabase

from app.error import SurveyAnswerTooLarge

from app._typing import MTurkID


class User(AbstractDatabase, BaseDatabase):
    
    @classmethod
    def get_all_documents(cls) -> None:
        return pyMongo.db.User.find({})
        
    @classmethod
    def search_document(
        cls, mturk_id: MTurkID
    ) -> None:

        return pyMongo.db.User.find_one({
            'mturk_id': mturk_id
        })

    @classmethod
    def create_document(
        cls, mturk_id: MTurkID
    ) -> None:

        voter_document = {
            'mturk_id': mturk_id,
            'participated_survey_template_id': {}
        },
        
        if not if_file_size_exceed_limit(file=voter_document):
            raise SurveyAnswerTooLarge

        return pyMongo.db.User.insert_one(voter_document)
    
    @classmethod
    def update_document(
        cls, 
        mturk_id: MTurkID, 
        survey_template_id: str, 
        survey_answer_id: str
    ) -> None:

        return pyMongo.db.User.update_one({'mturk_id': mturk_id}, {'$set':{
                   f'participated_survey_template_id.{survey_template_id}.{survey_answer_id}': True
               }})
    
    @classmethod
    def delete_document(
        cls, mturk_id: MTurkID
    ) -> None:

        '''
        Delete corresponding record
        '''

        return pyMongo.db.User.delete_one({'mturk_id': mturk_id})