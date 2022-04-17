from app import pyMongo
from app.mongoDB.utils import *

from app.mongoDB.mongoDBAbstractOperator import mongoDBAbstractOperator

class SurveyTemplate(mongoDBAbstractOperator):

    @classmethod
    def search_document(cls, survey_template_id):
        return pyMongo.db.SurveyTemplate.find_one({'survey_template_id': survey_template_id})

    @classmethod
    def create_document(cls, survey_template_id, survey_topic):
        '''
        survey_topic is a dictionary
        '''
        survey_template_document = {
            'survey_template_id': survey_template_id,
            'survey_topic': survey_topic,
        }
        indicator, BSON_file = if_file_size_exceed_limit(file=survey_template_document)
        if indicator:
            raise ValueError('Answer is too large')
        return pyMongo.db.SurveyTemplate.insert_one(survey_template_document)
    
    @classmethod
    def update_document(cls, survey_template_id, survey_topic):
        return pyMongo.db.Voter.update_one({'survey_template_id': survey_template_id}, {'$set':{
                   'survey_topic': survey_topic
               }})
    
    @classmethod
    def delete_document(cls, survey_template_id):
        return pyMongo.db.SurveyTemplate.delete_one({'survey_template_id': survey_template_id})