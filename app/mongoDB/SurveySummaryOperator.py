from app import pyMongo
from app.mongoDB.utils import *

from app.mongoDB.mongoDBAbstractOperator import mongoDBAbstractOperator

class SurveySummary(mongoDBAbstractOperator):

    @classmethod
    def search_document(cls, identifier_id):
        return pyMongo.db.SurveySummary.find_one({'identifier_id': identifier_id})

    @classmethod
    def create_document(cls, survey_template_id, survey_topic):
        survey_summary_document = {
            'survey_template_id': survey_template_id,
            'survey_topic': survey_topic,
        }

        indicator, BSON_file = if_file_size_exceed_limit(file=survey_summary_document)
        if indicator:
            raise ValueError('Answer is too large')
        return pyMongo.db.SurveySummary.insert_one(survey_summary_document)
    
    @classmethod
    def update_document(cls, survey_template_id, survey_topic):
        return pyMongo.db.SurveySummary.update_one({'survey_template_id': survey_template_id}, {'$set':{
                   'survey_topic': survey_topic
               }})
    
    @classmethod
    def delete_document(cls, survey_template_id):
        return pyMongo.db.SurveySummary.delete_one({'survey_template_id': survey_template_id})