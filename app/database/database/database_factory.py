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

    @classmethod
    @abstractmethod
    def get_instance(cls):
        pass


class GetSurveyAnswer(AbstractDatabaseFactory):

    @classmethod
    def get_instance(cls) -> type[SurveyAnswer]:
        return SurveyAnswer


class GetSurveySummary(AbstractDatabaseFactory):

    @classmethod
    def get_instance(cls) -> type[SurveySummary]:
        return SurveySummary


class GetSurveyTemplate(AbstractDatabaseFactory):

    @classmethod
    def get_instance(cls) -> type[SurveyTemplate]:
        return SurveyTemplate


class GetVoter(AbstractDatabaseFactory):

    @classmethod
    def get_instance(cls) -> type[Voter]:
        return Voter

class GetUser(AbstractDatabaseFactory):

    @classmethod
    def get_instance(cls) -> type[User]:
        return User