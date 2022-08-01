from __future__ import annotations

from app import pyMongo

from app.database.database.base import BaseDatabase

from app.database.database.abstract_database import AbstractDatabase

from app.utils.api import Serialization

from datetime import datetime

from pymongo.results import (
    InsertOneResult,
    UpdateResult,
    DeleteResult
)

from pymongo.cursor import Cursor

from typeguard import typechecked

from typing import (
    Any,
    Union
)

from app._typing import (
    Survey_Update_Method,
    Survey_Topics,
    Survey_Prev_Answers,
    Survey_New_Answers
)


@typechecked
class SurveyTemplate(AbstractDatabase, BaseDatabase):
    '''
    Manage the SurveyTemplate collection in DB

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
        return pyMongo.db.SurveyTemplate.estimated_document_count()

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
        return pyMongo.db.SurveyTemplate.find({})

    @classmethod
    def search_document(
        cls, survey_template_id: str
    ) -> Union[None, dict[str, Any]]:
        '''
        Search and return SurveyAnswer document
        In case of no matches this method returns nothing,
        otherwise return the matched document(dict form).

        Parameters
        ----------
        survey_template_id : str

        Returns
        -------
        dict
        '''
        return pyMongo.db.SurveyTemplate.find_one({
            'survey_template_id': survey_template_id
        })

    @classmethod
    def create_document(
        cls, 
        survey_template_id: str, 
        survey_template_name: str,
        survey_update_method: Survey_Update_Method,
        creation_time: int,
        expiration_time: int,
        time_period: str,
        number_of_copies: int,
        max_rounds: int,
        survey_topics: Survey_Topics
    ) -> InsertOneResult:
        '''
        Create Survey_Template document

        Parameters
        ----------
        survey_template_id : str
        survey_template_name : str
        survey_update_method : Survey_Update_Method
        creation_time : int
        expiration_time : int
        time_period : str
        number_of_copies : int
        max_rounds : int
        survey_topics : Survey_Topics

        Returns
        -------
        None
        '''
        survey_template_document = {
            'survey_template_id': survey_template_id,
            'survey_template_name': survey_template_name,
            'survey_update_method': survey_update_method,
            'creation_time': creation_time,
            'expiration_time': expiration_time,
            'time_period': time_period,
            'number_of_copies': number_of_copies,
            'max_rounds': max_rounds,
            'survey_topics': survey_topics,
        }
        
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
    ) -> DeleteResult:
        '''
        Delete corresponding document

        Parameters
        ----------
        survey_template_id : str

        Returns
        -------
        None
        '''
        return pyMongo.db.SurveyTemplate.delete_one({
            'survey_template_id': survey_template_id
        })