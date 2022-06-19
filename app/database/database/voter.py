from __future__ import annotations

from app import pyMongo

from app.database.database.base import BaseDatabase

from app.database.database.abstract_database import AbstractDatabase

from typeguard import typechecked

from app._typing import MTurkID

from typing import Any

@typechecked
class Voter(AbstractDatabase, BaseDatabase):
    '''
    Manage the Voter collection in DB

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
        return pyMongo.db.Voter.estimated_document_count()

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
        return pyMongo.db.Voter.find({})
        
    @classmethod
    def search_document(
        cls, mturk_id: MTurkID
    ) -> dict[str, Any]:
        '''
        Search unique Voter document

        Parameters
        ----------
        survey_answer_id : str

        Returns
        -------
        dict
        '''
        return pyMongo.db.Voter.find_one({
            'mturk_id': mturk_id
        })

    @classmethod
    def create_document(
        cls, mturk_id: MTurkID
    ) -> None:

        voter_document = {
            'mturk_id': mturk_id,
            'participated_survey_template_id': {}
        }

        pyMongo.db.Voter.insert_one(voter_document)
        return

    @classmethod
    def update_document(
        cls, 
        mturk_id: MTurkID, 
        survey_template_id: str, 
        survey_answer_id: str
    ) -> None:
        '''
        Voter can participate in many survey template answer.
        Voter collection records this in db.

        Parameters
        ----------
        mturk_id : MTurkID
        survey_template_id : str
        survey_answer_id : str

        Returns
        -------
        None
        '''
        pyMongo.db.Voter.update_one({'mturk_id': mturk_id}, {'$set':{
                f'participated_survey_template_id.{survey_template_id}.{survey_answer_id}': True
            }})
        return
    
    @classmethod
    def delete_document(
        cls, mturk_id: MTurkID
    ) -> None:
        '''
        Delete corresponding record

        Parameters
        ----------
        survey_answer_id : str

        Returns
        -------
        None
        '''

        pyMongo.db.Voter.delete_one({'mturk_id': mturk_id})
        return