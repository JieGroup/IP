from __future__ import annotations

from app.database.strategy.abstract_database_strategy import AbstractDatabaseStrategy

from app.database.strategy.base import BaseDatabaseStrategy

from app.database.database.api import (
    GetSurveyAnswer,
    GetSurveySummary,
    GetSurveyTemplate,
    GetVoter,
    GetUser
)

from pymongo.results import (
    InsertOneResult,
    UpdateResult,
    DeleteResult
)

from pymongo.cursor import Cursor

from typeguard import typechecked

from typing import Union

from app._typing import (
    Database_Type
)

@typechecked
class DatabaseOperator(AbstractDatabaseStrategy, BaseDatabaseStrategy):
    '''
    Strategy pattern to manage DB

    Attributes
    ----------
    database

    Methods
    -------
    set_database
    get_all_documents
    search_document
    create_document
    update_document
    delete_document
    '''
    def __init__(self) -> None:
        self.__database_operator = None

    @property
    def database(self) -> object:
        '''
        get strategy object
    
        Parameters
        ----------
        None

        Returns
        -------
        object
        '''
        return self.__database_operator

    @database.setter
    def database(
        self, database: object
    ) -> None:
        '''
        set database to a strategy object

        Parameters
        ----------
        database : object

        Returns
        -------
        dict
        '''
        self.__database_operator = database
        return

    def set_database(
        self, database_type: Database_Type
    ) -> None:
        '''
        function to help set strategy object

        Parameters
        ----------
        database_type : Database_Type

        Returns
        -------
        None
        '''
        if database_type == 'survey_answer':
            self.__database_operator = GetSurveyAnswer.get_class()
        elif database_type == 'survey_summary':
            self.__database_operator = GetSurveySummary.get_class()
        elif database_type == 'survey_template':
            self.__database_operator = GetSurveyTemplate.get_class()
        elif database_type == 'voter':
            self.__database_operator = GetVoter.get_class()
        elif database_type == 'user':
            self.__database_operator = GetUser.get_class()
        return

    def get_all_documents_count(
        self, **kwargs
    ) -> int:
        '''
        strategy interface
        '''
        return self.__database_operator.get_all_documents_count(**kwargs)

    def get_all_documents(
        self, **kwargs
    ) -> Cursor:
        '''
        strategy interface
        '''
        return self.__database_operator.get_all_documents(**kwargs)
    
    def search_document(
        self, **kwargs
    ) -> Union[None, dict]:
        '''
        strategy interface and check mongodb response

        Notes
        -----
        search_document doest not need to check all the time,
        since we may use it to check if the username is duplicated(the
        return value can be None), etc.
        '''
        res = self.__database_operator.search_document(**kwargs)
        if 'check_response' in kwargs and not kwargs['check_response']:
            return res
        super().check_search_document_response(res=res)
        return res
    
    def search_multiple_documents(
        self, **kwargs
    ) -> Cursor:
        '''
        strategy interface and check mongodb response

        Notes
        -----
        search_document doest not need to check all the time,
        since we may use it to check if the username is duplicated(the
        return value can be None), etc.
        '''
        res = self.__database_operator.search_multiple_documents(**kwargs)
        if 'check_response' in kwargs and not kwargs['check_response']:
            return res
        super().check_search_document_response(res=res)
        return res
    
    def create_document(
        self, **kwargs
    ) -> InsertOneResult:
        '''
        strategy interface and check mongodb response
        '''
        res = self.__database_operator.create_document(**kwargs)
        super().check_create_document_response(res=res)
        return res

    def update_document(
        self, **kwargs
    ) -> UpdateResult:
        '''
        strategy interface and check mongodb response
        '''
        res = self.__database_operator.update_document(**kwargs)
        super().check_update_document_response(res=res)
        return res
    
    def delete_document(
        self, **kwargs
    ) -> DeleteResult:
        '''
        strategy interface and check mongodb response
        '''
        res = self.__database_operator.delete_document(**kwargs)
        super().check_delete_document_response(res=res)
        return res