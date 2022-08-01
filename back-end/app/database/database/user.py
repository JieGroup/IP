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
        cls, **kwargs: Any
    ) -> Union[None, dict[str, Any]]:
        '''
        Search unique user document.
        In case of no matches this method returns nothing,
        otherwise return the matched document(dict form).

        Parameters
        ----------
        user_id : str

        Returns
        -------
        None or dict.
            Return None when db cannot find the
            document, otherwise return dict.
        '''
        if 'user_id' in kwargs:
            return pyMongo.db.User.find_one({
                'user_id': kwargs['user_id']
            })
        elif 'username' in kwargs:
            return pyMongo.db.User.find_one({
                'username': kwargs['username']
            })
        elif 'email' in kwargs:
            return pyMongo.db.User.find_one({
                'email': kwargs['email']
            })
        else:
            raise ValueError(
                'wrong key used in searching user document'
            )

    @classmethod
    def create_document(
        cls, 
        user_id: str,
        username: str,
        email: str,
        hashed_password: str,
        authority_level: str,
        comfirm_email: bool,
        designed_survey_template: dict={}
    ) -> InsertOneResult:
        '''
        Create user document

        Parameters
        ----------
        user_id : str
        username : str
        email : str
        hashed_password : str
        authority_level : str
        comfirm_email : bool
        designed_survey_template : dict

        Returns
        -------
        InsertOneResult
        '''
        user_document = {
            'user_id': user_id,
            'username': username,
            'email': email,
            'hashed_password': hashed_password,
            'authority_level': authority_level,
            'comfirm_email': comfirm_email,
            'designed_survey_template': designed_survey_template
        }

        return pyMongo.db.User.insert_one(user_document)
    
    @classmethod
    def update_document(
        cls, 
        user_id: str,
        **kwargs
    ) -> UpdateResult:
        # confirm email
        if 'confirm_email' in kwargs:
            return pyMongo.db.User.update_one({'user_id': user_id}, {'$set':{
                f'confirm_email': kwargs['confirm_email']
            }})
        # record the survey template created by current user
        elif 'survey_template_id' in kwargs:
            survey_template_id = kwargs['survey_template_id']
            survey_template_name = kwargs['survey_template_id']
            creation_time = kwargs['creation_time']
            expiration_time = kwargs['expiration_time']
            return pyMongo.db.User.update_one({'user_id': user_id}, {'$set':{
                f'designed_survey_templates.{survey_template_id}': {
                    'survey_template_name': survey_template_name,
                    'creation_time': creation_time,
                    'expiration_time': expiration_time
                }
            }})
        # reset password
        elif 'hashed_password' in kwargs:
            return pyMongo.db.User.update_one({'user_id': user_id}, {'$set':{
                f'hashed_password': kwargs['hashed_password']
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