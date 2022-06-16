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

from typing import Union

from app._typing import (
    Database_Type
)


class DatabaseOperator(AbstractDatabaseStrategy, BaseDatabaseStrategy):
    # __DatabaseOperator_instance = None
    # strategy pattern
    # 传给他不同的行为，algo使用

    def __init__(self) -> None:
        self.__database_operator = None

    # @classmethod
    # def get_instance(cls) -> type[DatabaseOperator]:
    #     if cls.__DatabaseOperator_instance == None:
    #         cls.__DatabaseOperator_instance = DatabaseOperator()

    #     return cls.__DatabaseOperator_instance

    @property
    def database(self):
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self.__database_operator

    @database.setter
    def database(self, database) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self.__database_operator = database

    def set_database(
        self, database_type: Database_Type
    ) -> None:
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

    def get_all_documents(
        self, **kwargs
    ) -> list:
        return self.__database_operator.get_all_documents(**kwargs)
    
    def search_document(
        self, **kwargs
    ) -> list:
        return self.__database_operator.search_document(**kwargs)
    
    def create_document(
        self, **kwargs
    ) -> list:
        return self.__database_operator.create_document(**kwargs)

    def update_document(
        self, **kwargs
    ) -> list:
        return self.__database_operator.update_document(**kwargs)
    
    def delete_document(
        self, **kwargs
    ) -> list:
        return self.__database_operator.delete_document(**kwargs)