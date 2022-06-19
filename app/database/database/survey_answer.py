from __future__ import annotations

from app import pyMongo

from app.database.database.base import BaseDatabase

from app.database.database.abstract_database import AbstractDatabase

from typeguard import typechecked

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
    ) -> list[dict[str, Any]]:
        '''
        Return the all documents based on
        conditions

        Parameters
        ----------
        None

        Returns
        -------
        list[dict[str, Any]]
        '''
        if 'survey_template_id' in kwargs:
            return pyMongo.db.SurveyAnswer.find({
                'survey_template_id': kwargs['survey_template_id']
            })
        res = pyMongo.db.SurveyAnswer.find({})
        print('***', res, type(res))
        return res

    @classmethod
    def search_document(
        cls, survey_answer_id: str
    ) -> Union[None, dict[str, Any]]:
        '''
        Search unique SurveyAnswer document

        Parameters
        ----------
        survey_answer_id : str

        Returns
        -------
        None or dict.
            Return None when db cannot find the
            document, otherwise return dict.
        '''
        res = pyMongo.db.SurveyAnswer.find_one({
            'survey_answer_id': survey_answer_id
        })
        print(f'search_document: {res}', type(res))
        return res

    @classmethod
    def create_document(
        cls, 
        survey_answer_id: str, 
        survey_template_id: str, 
        mturk_id: MTurkID, 
    ) -> None:
        '''
        Create Survey_Answer document

        Parameters
        ----------
        survey_answer_id : str
        survey_template_id : str 
        mturk_id : str

        Returns
        -------
        None
        '''
        survey_answer_document = {
            'survey_answer_id': survey_answer_id,
            'survey_template_id': survey_template_id,
            'mturk_id': mturk_id,
            'survey_answers': {},
        }
        
        pyMongo.db.SurveyAnswer.insert_one(survey_answer_document)
        return

    @classmethod
    def update_document(
        cls, 
        cur_rounds_num: int,
        survey_answer_id: str,
        survey_new_answers: dict[str, Union[str, dict[str, Any]]], 
    ) -> None:
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
        None
        '''

        rounds_key = f'rounds_{cur_rounds_num}'
        pyMongo.db.SurveyAnswer.update_one({'survey_answer_id': survey_answer_id}, {'$set':{
            f'survey_answers.{rounds_key}': survey_new_answers,
        }})
        return 

    @classmethod
    def delete_document(
        cls, survey_answer_id: str
    ) -> None:
        '''
        delete specific document

        Parameters
        ----------
        survey_answer_id : str

        Returns
        -------
        None
        '''

        pyMongo.db.SurveyAnswer.delete_one({
            'survey_answer_id': survey_answer_id
        })
        return
