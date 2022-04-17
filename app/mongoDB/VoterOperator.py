from app import pyMongo
from app.mongoDB.utils import *

from app.mongoDB.mongoDBAbstractOperator import mongoDBAbstractOperator

class Voter(mongoDBAbstractOperator):

    @classmethod
    def document_count(cls):
        return pyMongo.db.Voter.count()
    
    @classmethod
    def all_documents(cls):
        return pyMongo.db.Voter.find({})
        
    @classmethod
    def search_document(cls, mturk_id):
        return pyMongo.db.Voter.find_one({'mturk_id': mturk_id})

    @classmethod
    def create_document(cls, mturk_id, participated_survey_template_id={}):
        voter_document = {
            'mturk_id': mturk_id,
            'participated_survey_template_id': participated_survey_template_id,
        }
        indicator, BSON_file = if_file_size_exceed_limit(file=voter_document)
        if indicator:
            raise ValueError('Answer is too large')
        return pyMongo.db.Voter.insert_one(voter_document)
    
    @classmethod
    def update_document(cls, mturk_id, survey_template_id, survey_answer_id):
        return pyMongo.db.Voter.update_one({'mturk_id': mturk_id}, {'$set':{
                #    'participated_survey_template_id.' + str(survey_template_id) + '.' + str(survey_answer_id): True
                   f'participated_survey_template_id.{survey_template_id}.{survey_answer_id}': True
               }})
    
    @classmethod
    def delete_document(cls, mturk_id):
        return pyMongo.db.Voter.delete_one({'mturk_id': mturk_id})