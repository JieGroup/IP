from __future__ import annotations

from app import pyMongo
from app.database.utils import (
    if_file_size_exceed_limit
)

from app.database.database.base import BaseDatabase

from app.database.database.abstract_database import AbstractDatabase

from app._typing import MTurkID


class Voter(AbstractDatabase, BaseDatabase):

    @classmethod
    def get_all_documents_count(cls) -> None:
        return pyMongo.db.Voter.estimated_document_count()
    
    @classmethod
    def get_all_documents(cls) -> None:
        return pyMongo.db.Voter.find({})
        
    @classmethod
    def search_document(
        cls, mturk_id: MTurkID
    ) -> None:

        return pyMongo.db.Voter.find_one({'mturk_id': mturk_id})

    @classmethod
    def create_document(
        cls, mturk_id: MTurkID
    ) -> None:

        voter_document = {
            'mturk_id': mturk_id,
            'participated_survey_template_id': {}
        },
        
        indicator, BSON_file = if_file_size_exceed_limit(file=voter_document)
        if indicator:
            raise ValueError('Answer is too large')

        return pyMongo.db.Voter.insert_one(voter_document)
    
    @classmethod
    def update_document(
        cls, 
        mturk_id: MTurkID, 
        survey_template_id: str, 
        survey_answer_id: str
    ) -> None:

        return pyMongo.db.Voter.update_one({'mturk_id': mturk_id}, {'$set':{
                   f'participated_survey_template_id.{survey_template_id}.{survey_answer_id}': True
               }})
    
    @classmethod
    def delete_document(
        cls, mturk_id
    ) -> None:
    
        return pyMongo.db.Voter.delete_one({'mturk_id': mturk_id})