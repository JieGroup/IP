from app import pyMongo
from app.mongoDB.utils import *

from app.mongoDB.mongoDBAbstractOperator import mongoDBAbstractOperator

class SurveyAnswer(mongoDBAbstractOperator):

    @classmethod
    def get_all_documents_count(cls, **kwargs):
        if 'way' in kwargs:
            return pyMongo.db.SurveyAnswer.count_documents({'way': kwargs['way']})
        else:
            # print(dir(pyMongo.db.SurveyAnswer))
            return pyMongo.db.SurveyAnswer.estimated_document_count()

    @classmethod
    def get_all_documents(cls, **kwargs):
        if 'mturk_id' in kwargs and 'way' in kwargs:
            return pyMongo.db.SurveyAnswer.find({'mturk_id': kwargs['mturk_id'], 'way': kwargs['way']})
        else:
            return pyMongo.db.SurveyAnswer.find({})

    @classmethod
    def search_document(cls, **kwargs):
        if 'survey_answer_id' in kwargs:
            return pyMongo.db.SurveyAnswer.find_one({'survey_answer_id': kwargs['survey_answer_id']})
        elif 'digits' in kwargs:
            return pyMongo.db.SurveyAnswer.find_one({'digits': kwargs['digits']})
        else:
            raise ValueError('Please input correct SurveyAnswer key')


    @classmethod
    def create_document(cls, survey_answer_id, survey_template_id, mturk_id, way, digits):
        # calculate survey_round
        prev_survey_round = pyMongo.db.SurveyAnswer.count_documents({'survey_template_id': survey_template_id, 'mturk_id': mturk_id})
        print(f'prev_survey_round: {prev_survey_round}')
        survey_round = prev_survey_round + 1
        survey_answer_document = {
            'survey_answer_id': survey_answer_id,
            'survey_template_id': survey_template_id,
            'mturk_id': mturk_id,
            'survey_round': survey_round,
            'way': way,
            'digits': digits,
            'survey_answers': {},
        }
        indicator, BSON_file = if_file_size_exceed_limit(file=survey_answer_document)
        if indicator:
            raise ValueError('Answer is too large')
        return pyMongo.db.SurveyAnswer.insert_one(survey_answer_document)
    
    @classmethod
    def update_document(cls, digits, survey_topic, survey_answer, start_time, end_time, answer_type):
        if survey_topic == 'MTurk':
            return pyMongo.db.SurveyAnswer.update_one({'digits': digits}, {'$set':{
                #    'survey_answers.' + str(survey_key) + '.' + rounds_key: survey_answer
                    'mturk_id': survey_answer,
                }})
        else:
            survey_answer_document = cls.search_document(digits=digits)
            cur_round = 1
            if survey_topic in survey_answer_document['survey_answers']:
                cur_round = len(survey_answer_document['survey_answers'][survey_topic]) + 1
            rounds_key = 'rounds_' + str(cur_round)
            # print('lihai{survey_answer_document}+{cur_round}')
            return pyMongo.db.SurveyAnswer.update_one({'digits': digits}, {'$set':{
                #    'survey_answers.' + str(survey_key) + '.' + rounds_key: survey_answer
                    f'survey_answers.{survey_topic}.{rounds_key}.start_time': start_time,
                    f'survey_answers.{survey_topic}.{rounds_key}.end_time': end_time,
                    f'survey_answers.{survey_topic}.{rounds_key}.answer': survey_answer,
                    f'survey_answers.{survey_topic}.{rounds_key}.answer_type': answer_type,
                }})

    
    @classmethod
    def delete_document(cls, survey_answer_id):
        return pyMongo.db.SurveyAnswer.delete_one({'survey_answer_id': survey_answer_id})
