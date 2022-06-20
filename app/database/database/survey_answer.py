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
class SurveyAnswer(AbstractDatabase, BaseDatabase):
    '''
    Manage the SurveyAnswer collection in DB

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
        return pyMongo.db.SurveyAnswer.estimated_document_count()

    @classmethod
    def get_all_documents(
        cls, **kwargs
    ) -> Cursor:
        '''
        Return the all documents based on
        conditions

        Parameters
        ----------
        None

        Returns
        -------
        Cursor
        '''
        if 'survey_template_id' in kwargs:
            return pyMongo.db.SurveyAnswer.find({
                'survey_template_id': kwargs['survey_template_id']
            })
        return pyMongo.db.SurveyAnswer.find({})

    @classmethod
    def search_document(
        cls, survey_answer_id: str
    ) -> Union[None, dict[str, Any]]:
        '''
        Search unique SurveyAnswer document.
        In case of no matches this method returns nothing,
        otherwise return the matched document(dict form).

        Parameters
        ----------
        survey_answer_id : str

        Returns
        -------
        None or dict.
            Return None when db cannot find the
            document, otherwise return dict.
        '''
        return pyMongo.db.SurveyAnswer.find_one({
            'survey_answer_id': survey_answer_id
        })

    @classmethod
    def create_document(
        cls, 
        survey_answer_id: str, 
        survey_template_id: str, 
        mturk_id: MTurkID, 
    ) -> InsertOneResult:
        '''
        Create Survey_Answer document

        Parameters
        ----------
        survey_answer_id : str
        survey_template_id : str 
        mturk_id : str

        Returns
        -------
        InsertOneResult
        '''
        survey_answer_document = {
            'survey_answer_id': survey_answer_id,
            'survey_template_id': survey_template_id,
            'mturk_id': mturk_id,
            'survey_answers': {},
        }
        
        return pyMongo.db.SurveyAnswer.insert_one(survey_answer_document)

    @classmethod
    def update_document(
        cls, 
        cur_rounds_num: int,
        survey_answer_id: str,
        survey_new_answers: dict[str, Union[str, dict[str, Any]]], 
    ) -> UpdateResult:
        '''
        Update unique document
        Voter can answer dynamic topics in a survey template multiple times.
        We need to store the answers at each round.

        Parameters
        ----------
        cur_rounds_num : int
        survey_answer_id : str
        survey_new_answers : dict

        Returns
        -------
        UpdateResult
        '''
        rounds_key = f'rounds_{cur_rounds_num}'
        return pyMongo.db.SurveyAnswer.update_one({'survey_answer_id': survey_answer_id}, {'$set':{
            f'survey_answers.{rounds_key}': survey_new_answers,
        }})

    @classmethod
    def delete_document(
        cls, survey_answer_id: str
    ) -> DeleteResult:
        '''
        Delete specific document

        Parameters
        ----------
        survey_answer_id : str

        Returns
        -------
        DeleteResult
        '''
        return pyMongo.db.SurveyAnswer.delete_one({
            'survey_answer_id': survey_answer_id
        })