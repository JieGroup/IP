from abc import ABC, abstractmethod

from app.mongoDB.SurveyAnswerOperator import SurveyAnswer
from app.mongoDB.SurveySummaryOperator import SurveySummary
from app.mongoDB.SurveyTemplateOperator import SurveyTemplate
from app.mongoDB.VoterOperator import Voter

class MongoDBAbstractFactory(ABC):

    @classmethod
    @abstractmethod
    def create_mongoDB_operator(cls):
        pass

class SurveyAnswerFactory(MongoDBAbstractFactory):

    @classmethod
    def create_mongoDB_operator(cls):
        return SurveyAnswer

class SurveySummaryFactory(MongoDBAbstractFactory):

    @classmethod
    def create_mongoDB_operator(cls):
        return SurveySummary

class SurveyTemplateFactory(MongoDBAbstractFactory):

    @classmethod
    def create_mongoDB_operator(cls):
        return SurveyTemplate

class VoterFactory(MongoDBAbstractFactory):

    @classmethod
    def create_mongoDB_operator(cls):
        return Voter

