from __future__ import annotations

from app.database.strategy.abstract_database_strategy import AbstractDatabaseStrategy

from app.database.strategy.base import BaseDatabaseStrategy

from app.database.database.database_factory import (
    GetSurveyAnswer,
    GetSurveySummary,
    GetSurveyTemplate,
    GetVoter,
    GetUser
)

from app.utils.dtypes.api import is_var_in_literal

from typeguard import typechecked

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
        if not is_var_in_literal(
            var=database_type,
            expected_type=Database_Type
        ):
            raise ValueError('database_type is wrong')

        if database_type == 'survey_answer':
            self.__database_operator = GetSurveyAnswer.get_instance()
        elif database_type == 'survey_summary':
            self.__database_operator = GetSurveySummary.get_instance()
        elif database_type == 'survey_template':
            self.__database_operator = GetSurveyTemplate.get_instance()
        elif database_type == 'voter':
            self.__database_operator = GetVoter.get_instance()
        elif database_type == 'user':
            self.__database_operator = GetUser.get_instance()
        return

    def get_all_documents(
        self, **kwargs
    ) -> list[dict]:
        '''
        strategy interface
        '''
        return self.__database_operator.get_all_documents(**kwargs)
    
    def search_document(
        self, **kwargs
    ) -> dict:
        '''
        strategy interface
        '''
        return self.__database_operator.search_document(**kwargs)
    
    def create_document(
        self, **kwargs
    ) -> None:
        '''
        strategy interface
        '''
        return self.__database_operator.create_document(**kwargs)

    def update_document(
        self, **kwargs
    ) -> None:
        '''
        strategy interface
        '''
        return self.__database_operator.update_document(**kwargs)
    
    def delete_document(
        self, **kwargs
    ) -> None:
        '''
        strategy interface
        '''
        return self.__database_operator.delete_document(**kwargs)