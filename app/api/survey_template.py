from app.api import api_bp

from flask import request
from flask.json import jsonify

from app.error import bad_request

from app.process.api import SurveyTemplate


@api_bp.route('/create_survey_template', methods=['POST'])
def create_survey_template() -> None:
    '''
    data got from json is dict[dict[str, ]], which has
    3 keys in data: topic name, topic category, topic range
    '''
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'survey_update_method' not in data or not data.get('survey_update_method'):
        return bad_request('survey_update_method is required.') 
    if 'time_period' not in data or not data.get('time_period'):
        return bad_request('time_period is required.') 
    if 'number_of_copies' not in data or not data.get('number_of_copies'):
        return bad_request('number_of_copies is required.')
    if 'survey_topics' not in data or not data.get('survey_topics'):
        return bad_request('survey_topics is required.')
    
    survey_update_method = data['survey_update_method']
    time_period = data['time_period']
    number_of_copies = data['number_of_copies']
    survey_topics = data['survey_topics']

    SurveyTemplate.create_survey_template(
        survey_update_method=survey_update_method,
        time_period=time_period,
        number_of_copies=number_of_copies,
        survey_topics=survey_topics
    )

    # check survey_content

@api_bp.route('/get_default_survey_template', methods=['GET'])
def get_default_survey_template() -> None:

    '''
    data got from json is dict[dict[str, ]], which has
    3 keys in data: topic name, topic category, topic range
    '''

    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    
    survey_topics = data['survey_topics']
    SurveyTemplate.create_survey_template(survey_topics=survey_topics)


    



    # check survey_content
# @api_bp.route('/update_survey_template', methods=['POST'])
# def update_survey_template():

#     '''
#     data got from json is dict[dict[str, ]], which has
#     3 keys in data: topic name, topic category, topic range
#     '''

#     data = request.get_json()
#     if not data:
#         return bad_request('You must post JSON data.')
#     if 'survey_template_id' not in data or not data.get('survey_template_id'):
#         return bad_request('survey_template_id is required.')
#     if 'root_key' not in data or not data.get('root_key'):
#         return bad_request('root_key is required.')

#     survey_template_id = data['survey_template_id']
#     root_key = data['root_key']

#     SurveyTemplate.update_survey_template(
#         survey_template_id=survey_template_id,
#         root_key=root_key
#     )



    
