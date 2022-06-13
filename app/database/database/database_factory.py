from __future__ import annotations

from abc import ABC, abstractmethod

from app.database.database.api import (
    SurveyAnswer,
    SurveySummary,
    SurveyTemplate,
    Voter
)


class AbstractDatabaseFactory(ABC):

    @classmethod
    @abstractmethod
    def get_database(cls):
        pass


class GetSurveyAnswer(AbstractDatabaseFactory):

    @classmethod
    def get_database(cls) -> type[SurveyAnswer]:
        return SurveyAnswer


class GetSurveySummary(AbstractDatabaseFactory):

    @classmethod
    def get_database(cls) -> type[SurveySummary]:
        return SurveySummary


class GetSurveyTemplate(AbstractDatabaseFactory):

    @classmethod
    def get_database(cls) -> type[SurveyTemplate]:
        return SurveyTemplate


class GetVoter(AbstractDatabaseFactory):

    @classmethod
    def get_database(cls) -> type[Voter]:
        return Voter

