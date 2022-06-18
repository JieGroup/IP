from __future__ import annotations

from abc import ABC, abstractmethod

from app.database.database.api import (
    SurveyAnswer,
    SurveySummary,
    SurveyTemplate,
    Voter,
    User
)


class AbstractDatabaseFactory(ABC):
    '''
    Abstract class for database factory class.
    This is where our database factory can override
    '''
    @classmethod
    @abstractmethod
    def get_instance(cls):
        pass


class GetSurveyAnswer(AbstractDatabaseFactory):
    '''
    factory pattern to handle initilization
    of SurveyAnswer class
    '''
    @classmethod
    def get_instance(cls) -> type[SurveyAnswer]:
        return SurveyAnswer


class GetSurveySummary(AbstractDatabaseFactory):
    '''
    factory pattern to handle initilization
    of SurveySummary class
    '''
    @classmethod
    def get_instance(cls) -> type[SurveySummary]:
        return SurveySummary


class GetSurveyTemplate(AbstractDatabaseFactory):
    '''
    factory pattern to handle initilization
    of SurveyTemplate class
    '''
    @classmethod
    def get_instance(cls) -> type[SurveyTemplate]:
        return SurveyTemplate


class GetVoter(AbstractDatabaseFactory):
    '''
    factory pattern to handle initilization
    of Voter class
    '''
    @classmethod
    def get_instance(cls) -> type[Voter]:
        return Voter

class GetUser(AbstractDatabaseFactory):
    '''
    factory pattern to handle initilization
    of User class
    '''
    @classmethod
    def get_instance(cls) -> type[User]:
        return User