from app.mongoDB.mongoDBFactory.mongoDBFactory import SurveyAnswerFactory, SurveySummaryFactory, SurveyTemplateFactory, VoterFactory

def select_mongoDB_operator(collection_name: str):
    if collection_name == 'SurveyAnswer':
        return SurveyAnswerFactory.create_mongoDB_operator()
    elif collection_name == 'SurveySummary':
        return SurveySummaryFactory.create_mongoDB_operator()
    elif collection_name == 'SurveyTemplate':
        return SurveyTemplateFactory.create_mongoDB_operator()
    elif collection_name == 'Voter':
        return VoterFactory.create_mongoDB_operator()