from __future__ import annotations

from app import pyMongo

from app.database.database.base import BaseDatabase

from app.database.database.abstract_database import AbstractDatabase

from app.utils.api import Serialization

from datetime import datetime

from typing import Any


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
    def get_all_documents(cls) -> list[dict[str, Any]]:
        '''
        Return the all documents

        Parameters
        ----------
        None

        Returns
        -------
        list[dict[str, Any]]
        '''
        return pyMongo.db.SurveyTemplate.find({})

    @classmethod
    def search_document(
        cls, survey_template_id: str
    ) -> dict[str, Any]:
        '''
        Search and return SurveyAnswer document

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
        survey_update_method: str,
        expiration_time: type[datetime],
        number_of_copies: int,
        max_rounds: int,
        survey_topics: dict[dict[str, Any]]
    ) -> None:
        '''
        Create Survey_Template document

        Parameters
        ----------
        survey_template_id : str
        survey_update_method : str
        expiration_time : type[datetime]
        number_of_copies : int
        max_rounds : int
        survey_topics : dict[dict[str, Any]]

        Returns
        -------
        None
        '''
        survey_template_document = {
            'survey_template_id': survey_template_id,
            'survey_update_method': survey_update_method,
            'expiration_time': expiration_time,
            'number_of_copies': number_of_copies,
            'max_rounds': max_rounds,
            'survey_topics': survey_topics,
        }
        # TODO: make_data_serializable
        survey_template_document = Serialization.make_data_serializable(
            data=survey_template_document
        )
        
        pyMongo.db.SurveyTemplate.insert_one(survey_template_document)
        return 
    
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
        Delete corresponding document

        Parameters
        ----------
        survey_template_id : str

        Returns
        -------
        None
        '''
        pyMongo.db.SurveyTemplate.delete_one({
            'survey_template_id': survey_template_id
        })
        return