from app import pyMongo
from app.mongoDB.utils import *

from app.mongoDB.mongoDBAbstractOperator import mongoDBAbstractOperator

class SurveyAnswer(mongoDBAbstractOperator):

    @classmethod
    def search_document(cls, **kwargs):
        if 'survey_answer_id' in kwargs:
            return pyMongo.db.SurveyAnswer.find_one({'survey_answer_id': kwargs['survey_answer_id']})
        elif 'digits' in kwargs:
            return pyMongo.db.SurveyAnswer.find_one({'digits': kwargs['digits']})
        else:
            raise ValueError('Please input correct SurveyAnswer key')

    @classmethod
    def create_document(cls, survey_answer_id, survey_template_id, mturk_id, start_time, end_time, way, token):
        survey_answer_document = {
            'survey_answer_id': survey_answer_id,
            'survey_template_id': survey_template_id,
            'mturk_id': mturk_id,
            'start_time': start_time,
            'end_time': end_time,
            'way': way,
            'digits': token,
            'survey_answers': {},
        }
        indicator, BSON_file = if_file_size_exceed_limit(file=survey_answer_document)
        if indicator:
            raise ValueError('Answer is too large')
        return pyMongo.db.SurveyAnswer.insert_one(survey_answer_document)
    
    @classmethod
    def update_document(cls, survey_answer_id, survey_topic, survey_answer, start_time, end_time, answer_type):
        cur_round = len(cls.search_document(survey_answer_id)['survey_answers'][survey_topic]) + 1
        rounds_key = 'rounds_' + str(cur_round)
        return pyMongo.db.SurveyAnswer.update_one({'survey_answer_id': survey_answer_id}, {'$set':{
            #    'survey_answers.' + str(survey_key) + '.' + rounds_key: survey_answer
                f'survey_answers.{survey_topic}.{rounds_key}.start_time': start_time,
                f'survey_answers.{survey_topic}.{rounds_key}.end_time': end_time,
                f'survey_answers.{survey_topic}.{rounds_key}.answer': survey_answer,
                f'survey_answers.{survey_topic}.{rounds_key}.answer_type': answer_type,
            }})

    
    @classmethod
    def delete_document(cls, survey_answer_id):
        return pyMongo.db.SurveyAnswer.delete_one({'survey_answer_id': survey_answer_id})
