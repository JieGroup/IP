from __future__ import annotations

from abc import ABC, abstractmethod

from app.database.database.survey_answer import SurveyAnswer
from app.database.database.survey_summary import SurveySummary
from app.database.database.survey_template import SurveyTemplate
from app.database.database.voter import Voter
from app.database.database.user import User

from typeguard import typechecked


class AbstractDatabaseFactory(ABC):
    '''
    Abstract class for database factory class.
    This is where our database factory can override
    '''
    @classmethod
    @abstractmethod
    def get_class(cls):
        pass


@typechecked
class GetSurveyAnswer(AbstractDatabaseFactory):
    '''
    factory pattern to handle initilization
    of SurveyAnswer class
    '''
    @classmethod
    def get_class(cls) -> type[SurveyAnswer]:
        return SurveyAnswer


@typechecked
class GetSurveySummary(AbstractDatabaseFactory):
    '''
    factory pattern to handle initilization
    of SurveySummary class
    '''
    @classmethod
    def get_class(cls) -> type[SurveySummary]:
        return SurveySummary


@typechecked
class GetSurveyTemplate(AbstractDatabaseFactory):
    '''
    factory pattern to handle initilization
    of SurveyTemplate class
    '''
    @classmethod
    def get_class(cls) -> type[SurveyTemplate]:
        return SurveyTemplate


@typechecked
class GetVoter(AbstractDatabaseFactory):
    '''
    factory pattern to handle initilization
    of Voter class
    '''
    @classmethod
    def get_class(cls) -> type[Voter]:
        return Voter


@typechecked
class GetUser(AbstractDatabaseFactory):
    '''
    factory pattern to handle initilization
    of User class
    '''
    @classmethod
    def get_class(cls) -> type[User]:
        return User