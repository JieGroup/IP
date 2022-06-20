from __future__ import annotations

from app import pyMongo

from app.database.database.base import BaseDatabase

from app.database.database.abstract_database import AbstractDatabase

from typeguard import typechecked

from pymongo.results import (
    InsertOneResult,
    UpdateResult,
    DeleteResult
)

from pymongo.cursor import Cursor

from app._typing import MTurkID

from typing import (
    Union,
    Any
)


@typechecked
class User(AbstractDatabase, BaseDatabase):
    '''
    Manage the User collection in DB

    Attributes
    ----------
    None

    Methods
    -------
    get_all_documents_count
    get_all_documents
    search_document
    create_document
    update_document
    delete_document
    '''

    @classmethod
    def get_all_documents_count(cls) -> int:
        '''
        Return the count of all documents

        Parameters
        ----------
        None

        Returns
        -------
        int
        '''
        return pyMongo.db.User.estimated_document_count()

    @classmethod
    def get_all_documents(cls) -> Cursor:
        '''
        Return the all documents

        Parameters
        ----------
        None

        Returns
        -------
        Cursor
        '''
        return pyMongo.db.User.find({})
        
    @classmethod
    def search_document(
        cls, user_id: str
    ) -> Union[None, dict[str, Any]]:

        return pyMongo.db.User.find_one({
            'user_id': user_id
        })

    @classmethod
    def create_document(
        cls, mturk_id: MTurkID
    ) -> InsertOneResult:
        # TODO: modify this part
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
    ) -> UpdateResult:
        # TODO: modify this part
        return pyMongo.db.User.update_one({'mturk_id': mturk_id}, {'$set':{
                   f'participated_survey_template_id.{survey_template_id}.{survey_answer_id}': True
               }})
    
    @classmethod
    def delete_document(
        cls, user_id: str
    ) -> DeleteResult:
        '''
        delete corresponding document

        Parameters
        ----------
        user_id : str

        Returns
        -------
        None
        '''

        return pyMongo.db.User.delete_one({'user_id': user_id})