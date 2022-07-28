from __future__ import annotations

import json
import pytest
import requests

from tests.conftest import (
    get_test_client,
    get_token_auth_headers
)

from .utils import (
    get_api_url,
    select_first_option,
    stop_first_topic
)

from app.utils.api import Constant

from app.process.api import (
    SurveyTemplate,
    VoterAnswerSurvey
)

from app.error import DBDocumentNotFound


def answer_initilization(
    client,
    headers,
    survey_update_method,
    time_period,
    number_of_copies,
    max_rounds,
    survey_topics,
    mturk_id: str
) -> dict:
    '''
    Notes
    -----
    Include create_survey_template and voter_start_answering(get first round)
    '''
    data = json.dumps({
        'survey_update_method': survey_update_method,
        'time_period': time_period,
        'number_of_copies': number_of_copies,
        'max_rounds': max_rounds,
        'survey_topics': survey_topics
    })

    response = client.post(
        get_api_url('create_survey_template'), 
        headers=headers, 
        data=data
    )
    assert response.status_code == 200
    json_response = json.loads(response.get_data(as_text=True))
    survey_template_id = json_response['survey_template_id']

    data = json.dumps({
        'survey_template_id': survey_template_id,
        'mturk_id': mturk_id
    })
    response = client.post(
        get_api_url('voter_start_answering'), 
        headers=headers, 
        data=data
    )
    assert response.status_code == 200
    json_response = json.loads(response.get_data(as_text=True))
    return json_response


class TestVoterStartAnswering():

    @pytest.mark.parametrize(
        "method, time, number, rounds, survey_topics, mturk_id", 
        [
            (   
                'static',
                '3',
                Constant.MAX_NUMBER_OF_COPIES,
                Constant.MAX_ROUNDS,
                {
                    'age': {
                        'answer_type': 'continuous',
                        'continuous_range': {
                            'min': 0,
                            'max': 80
                        },
                        'topic_question': 'what is your age?',
                        'unit': 'y'
                    }
                }, 
                '123'
            ),
            (   
                'static',
                '3',
                Constant.MAX_NUMBER_OF_COPIES,
                Constant.MAX_ROUNDS,
                {
                    'age': {
                        'answer_type': 'categorical',
                        'categorical_range': {
                            'inclusion': [
                                1,
                                2,
                                '3',
                                4
                            ]
                        },
                        'topic_question': 'what is your choice?',
                        'unit': 'xx'
                    }
                }, 
                '1234'
            ),
            (   
                'uniform',
                '3',
                Constant.MAX_NUMBER_OF_COPIES,
                Constant.MAX_ROUNDS,
                {
                    'age': {
                        'answer_type': 'continuous',
                        'continuous_range': {
                            'min': 0,
                            'max': 80
                        },
                        'topic_question': 'what is your age?',
                        'unit': 'y'
                    }
                }, 
                '123'
            ),
            (   
                'uniform',
                '3',
                Constant.MAX_NUMBER_OF_COPIES,
                Constant.MAX_ROUNDS,
                {
                    'age': {
                        'answer_type': 'categorical',
                        'categorical_range': {
                            'inclusion': [
                                1,
                                2,
                                '3',
                                4
                            ]
                        },
                        'topic_question': 'what is your choice?',
                        'unit': 'xx'
                    }
                }, 
                '1234'
            ),
        ]
    )
    def test_start_answering(self, method, time, number, rounds, survey_topics, mturk_id):
        
        client = get_test_client()
        headers = get_token_auth_headers()
        json_response = answer_initilization(
            client=client,
            headers=headers,
            survey_update_method=method,
            time_period=time,
            number_of_copies=number,
            max_rounds=rounds,
            survey_topics=survey_topics,
            mturk_id=mturk_id
        )
        print('zzjson_response', json_response)
        assert 'voterToken' in json_response
        updated_survey_topics = json_response['updated_survey_topics'] 
        for key, val in survey_topics.items():
            assert val['answer_type'] == updated_survey_topics[key]['answer_type']
            assert val['topic_question'] == updated_survey_topics[key]['topic_question']
            assert val['unit'] == updated_survey_topics[key]['unit']

    # @pytest.mark.parametrize(
    #     "method, time, number, rounds, survey_topics, mturk_id", 
    #     [
    #         (   
    #             'static',
    #             '3',
    #             Constant.MAX_NUMBER_OF_COPIES,
    #             Constant.MAX_ROUNDS,
    #             {
    #                 'age': {
    #                     'answer_type': 'continuous',
    #                     'continuous_range': {
    #                         'min': 0,
    #                         'max': 80
    #                     },
    #                     'topic_question': 'what is your age?',
    #                     'unit': 'y'
    #                 }
    #             }, 
    #             '123'
    #         ),
    #         (   
    #             'static',
    #             '3',
    #             Constant.MAX_NUMBER_OF_COPIES,
    #             Constant.MAX_ROUNDS,
    #             {
    #                 'age': {
    #                     'answer_type': 'categorical',
    #                     'categorical_range': {
    #                         'inclusion': [
    #                             1,
    #                             2,
    #                             3,
    #                             4,
    #                             5,
    #                             6,
    #                             7,
    #                             8
    #                         ]
    #                     },
    #                     'topic_question': 'what is your choice?',
    #                     'unit': 'xx'
    #                 }
    #             }, 
    #             '1234'
    #         )
    #     ]
    # )
    # def test_voter_submit_answers_in_static_mode(self, method, time, number, rounds, survey_topics, mturk_id):
        
    #     client = get_test_client()
    #     headers = get_token_auth_headers()
    #     json_response = answer_initilization(
    #         client=client,
    #         headers=headers,
    #         survey_update_method=method,
    #         time_period=time,
    #         number_of_copies=number,
    #         max_rounds=rounds,
    #         survey_topics=survey_topics,
    #         mturk_id=mturk_id
    #     )

    #     survey_answer_id = json_response['survey_answer_id']
    #     updated_survey_topics = json_response['updated_survey_topics'] 
    #     print(f'!!updated_survey_topics: {updated_survey_topics}')
    #     for key, val in survey_topics.items():
    #         assert val['answer_type'] == updated_survey_topics[key]['answer_type']
    #         assert val['topic_question'] == updated_survey_topics[key]['topic_question']
    #         assert val['unit'] == updated_survey_topics[key]['unit']

    #     survey_new_answers = select_first_option(updated_survey_topics=updated_survey_topics)
    #     print(f'??survey_new_answers: {survey_new_answers}')
    #     data = json.dumps({
    #         'survey_answer_id': survey_answer_id,
    #         'survey_new_answers': survey_new_answers,
    #     })
    #     response = client.post(
    #         get_api_url('voter_submit_answers'), 
    #         headers=headers, 
    #         data=data
    #     )
    #     assert response.status_code == 200

    #     json_response = json.loads(response.get_data(as_text=True))
    #     survey_update_method = json_response['survey_update_method']
    #     updated_survey_topics = json_response['updated_survey_topics']
    #     survey_answer_id = json_response['survey_answer_id']
    #     # static topic only needs to be returned once
    #     assert updated_survey_topics == {}

    #     # msg = 'cannot input empty survey_new_answers'
    #     # with pytest.raises(ValueError, match=msg):
    #     data = json.dumps({
    #         'survey_answer_id': survey_answer_id,
    #         'survey_new_answers': updated_survey_topics,
    #     })
    #     response = client.post(
    #         get_api_url('voter_submit_answers'), 
    #         headers=headers, 
    #         data=data
    #     )
    #     json_response = json.loads(response.get_data(as_text=True))
    #     assert 'cannot input empty survey_new_answers' == json_response['error_msg']
    #     assert 'ValueError' == json_response['error_name']


    # @pytest.mark.parametrize(
    #     "method, time, number, rounds, survey_topics, mturk_id", 
    #     [
    #         (   
    #             'uniform',
    #             '3',
    #             Constant.MAX_NUMBER_OF_COPIES,
    #             Constant.MAX_ROUNDS,
    #             {
    #                 'age': {
    #                     'answer_type': 'continuous',
    #                     'continuous_range': {
    #                         'min': 0,
    #                         'max': 80
    #                     },
    #                     'topic_question': 'what is your age?',
    #                     'unit': 'y'
    #                 }
    #             }, 
    #             '123'
    #         ),
    #         (   
    #             'uniform',
    #             '3',
    #             Constant.MAX_NUMBER_OF_COPIES,
    #             Constant.MAX_ROUNDS,
    #             {
    #                 'age': {
    #                     'answer_type': 'categorical',
    #                     'categorical_range': {
    #                         'inclusion': [
    #                             1,
    #                             2,
    #                             3,
    #                             4,
    #                             5,
    #                             6,
    #                             7,
    #                             8
    #                         ]
    #                     },
    #                     'topic_question': 'what is your choice?',
    #                     'unit': 'xx'
    #                 }
    #             }, 
    #             '1234'
    #         ),
    #     ]
    # )
    # def test_voter_submit_answers_in_uniform_mode(self, method, time, number, rounds, survey_topics, mturk_id):
        
    #     client = get_test_client()
    #     headers = get_token_auth_headers()
    #     json_response = answer_initilization(
    #         client=client,
    #         headers=headers,
    #         survey_update_method=method,
    #         time_period=time,
    #         number_of_copies=number,
    #         max_rounds=rounds,
    #         survey_topics=survey_topics,
    #         mturk_id=mturk_id
    #     )

    #     survey_answer_id = json_response['survey_answer_id']
    #     updated_survey_topics = json_response['updated_survey_topics'] 
    #     for key, val in survey_topics.items():
    #         assert val['answer_type'] == updated_survey_topics[key]['answer_type']
    #         assert val['topic_question'] == updated_survey_topics[key]['topic_question']
    #         assert val['unit'] == updated_survey_topics[key]['unit']

    #     for round in range(1, Constant.MAX_ROUNDS):
    #         survey_new_answers = select_first_option(updated_survey_topics=updated_survey_topics)
    #         print(f'survey_new_answers: {survey_new_answers}')
    #         data = json.dumps({
    #             'survey_answer_id': survey_answer_id,
    #             'survey_new_answers': survey_new_answers,
    #         })

    #         response = client.post(
    #             get_api_url('voter_submit_answers'), 
    #             headers=headers, 
    #             data=data
    #         )
    #         assert response.status_code == 200

    #         json_response = json.loads(response.get_data(as_text=True))
    #         survey_update_method = json_response['survey_update_method']
    #         updated_survey_topics = json_response['updated_survey_topics']
    #         survey_answer_id = json_response['survey_answer_id']
    #         assert len(updated_survey_topics) != {}

    #     # msg = 'cannot input empty survey_new_answers'
    #     # with pytest.raises(ValueError, match=msg):
    #     survey_new_answers = select_first_option(updated_survey_topics=updated_survey_topics)
    #     data = json.dumps({
    #         'survey_answer_id': survey_answer_id,
    #         'survey_new_answers': survey_new_answers,
    #     })
    #     response = client.post(
    #         get_api_url('voter_submit_answers'), 
    #         headers=headers, 
    #         data=data
    #     )
    #     json_response = json.loads(response.get_data(as_text=True))
    #     print('jjj', json_response)
    #     updated_survey_topics = json_response['updated_survey_topics']
    #     # last round, should not update topics
    #     assert updated_survey_topics == {}

    # @pytest.mark.parametrize(
    #     "method, time, number, rounds, survey_topics, mturk_id", 
    #     [
    #         (   
    #             'uniform',
    #             '3',
    #             Constant.MAX_NUMBER_OF_COPIES,
    #             Constant.MAX_ROUNDS,
    #             {
    #                 'age_0': {
    #                     'answer_type': 'continuous',
    #                     'continuous_range': {
    #                         'min': 0,
    #                         'max': 80
    #                     },
    #                     'topic_question': 'what is your age?',
    #                     'unit': 'y'
    #                 },
    #                 'age_1': {
    #                     'answer_type': 'continuous',
    #                     'continuous_range': {
    #                         'min': 0,
    #                         'max': 80
    #                     },
    #                     'topic_question': 'what is your age?',
    #                     'unit': 'y'
    #                 },
    #                 'age_2': {
    #                     'answer_type': 'continuous',
    #                     'continuous_range': {
    #                         'min': 0,
    #                         'max': 80
    #                     },
    #                     'topic_question': 'what is your age?',
    #                     'unit': 'y'
    #                 }
    #             }, 
    #             '123'
    #         ),
    #         (   
    #             'uniform',
    #             '3',
    #             Constant.MAX_NUMBER_OF_COPIES,
    #             Constant.MAX_ROUNDS,
    #             {
    #                 'age_0': {
    #                     'answer_type': 'categorical',
    #                     'categorical_range': {
    #                         'inclusion': [
    #                             1,
    #                             2,
    #                             3,
    #                             4,
    #                             5,
    #                             6,
    #                             7,
    #                             8
    #                         ]
    #                     },
    #                     'topic_question': 'what is your choice?',
    #                     'unit': 'xx'
    #                 },
    #                 'age_1': {
    #                     'answer_type': 'categorical',
    #                     'categorical_range': {
    #                         'inclusion': [
    #                             1,
    #                             2,
    #                             3,
    #                             4,
    #                             5,
    #                             6,
    #                             7,
    #                             8
    #                         ]
    #                     },
    #                     'topic_question': 'what is your choice?',
    #                     'unit': 'xx'
    #                 },
    #                 'age_2': {
    #                     'answer_type': 'categorical',
    #                     'categorical_range': {
    #                         'inclusion': [
    #                             1,
    #                             2,
    #                             3,
    #                             4,
    #                             5,
    #                             6,
    #                             7,
    #                             8
    #                         ]
    #                     },
    #                     'topic_question': 'what is your choice?',
    #                     'unit': 'xx'
    #                 }
    #             }, 
    #             '1234'
    #         ),
    #     ]
    # )
    # def test_voter_submit_answers_in_uniform_mode_stop_exception(self, method, time, number, rounds, survey_topics, mturk_id):
    #     '''
    #     Test code when user stop any topic
    #     might be wrong if the new mid number is randomly chose as min_val
    #     '''
    #     client = get_test_client()
    #     headers = get_token_auth_headers()
    #     json_response = answer_initilization(
    #         client=client,
    #         headers=headers,
    #         survey_update_method=method,
    #         time_period=time,
    #         number_of_copies=number,
    #         max_rounds=rounds,
    #         survey_topics=survey_topics,
    #         mturk_id=mturk_id
    #     )

    #     survey_answer_id = json_response['survey_answer_id']
    #     updated_survey_topics = json_response['updated_survey_topics'] 
    #     for key, val in survey_topics.items():
    #         assert val['answer_type'] == updated_survey_topics[key]['answer_type']
    #         assert val['topic_question'] == updated_survey_topics[key]['topic_question']
    #         assert val['unit'] == updated_survey_topics[key]['unit']

    #     for round in range(1, Constant.MAX_ROUNDS):
    #         survey_new_answers = select_first_option(updated_survey_topics=updated_survey_topics)
    #         survey_new_answers, stop_key = stop_first_topic(survey_new_answers)
    #         print(f'~~survey_new_answers: {survey_new_answers}, {stop_key}')
    #         data = json.dumps({
    #             'survey_answer_id': survey_answer_id,
    #             'survey_new_answers': survey_new_answers,
    #         })

    #         response = client.post(
    #             get_api_url('voter_submit_answers'), 
    #             headers=headers, 
    #             data=data
    #         )
    #         assert response.status_code == 200

    #         json_response = json.loads(response.get_data(as_text=True))
    #         survey_update_method = json_response['survey_update_method']
    #         updated_survey_topics = json_response['updated_survey_topics']
    #         survey_answer_id = json_response['survey_answer_id']
    #         assert len(updated_survey_topics) != {}
    #         print(f'!!updated_survey_topics: {updated_survey_topics}')
    #         assert stop_key not in updated_survey_topics

    #     # msg = 'cannot input empty survey_new_answers'
    #     # with pytest.raises(ValueError, match=msg):
    #     survey_new_answers = select_first_option(updated_survey_topics=updated_survey_topics)
    #     data = json.dumps({
    #         'survey_answer_id': survey_answer_id,
    #         'survey_new_answers': survey_new_answers,
    #     })
    #     response = client.post(
    #         get_api_url('voter_submit_answers'), 
    #         headers=headers, 
    #         data=data
    #     )
    #     json_response = json.loads(response.get_data(as_text=True))
    #     print('jjj', json_response)
    #     updated_survey_topics = json_response['updated_survey_topics']
    #     # last round, should not update topics
    #     assert updated_survey_topics == {}

    # @pytest.mark.parametrize(
    #     "method, time, number, rounds, survey_topics, mturk_id", 
    #     [
    #         (   
    #             'uniform',
    #             '3',
    #             Constant.MAX_NUMBER_OF_COPIES,
    #             Constant.MAX_ROUNDS,
    #             {
    #                 'age_0': {
    #                     'answer_type': 'categorical',
    #                     'categorical_range': {
    #                         'inclusion': [
    #                             1,
    #                             2,
    #                             3,
    #                             4,
    #                             5,
    #                             6,
    #                             7,
    #                             8
    #                         ]
    #                     },
    #                     'topic_question': 'what is your choice?',
    #                     'unit': 'xx'
    #                 },
    #             }, 
    #             '1234'
    #         ),
    #     ]
    # )
    # def test_voter_submit_answers_in_uniform_mode_stop_exception(self, method, time, number, rounds, survey_topics, mturk_id):
    #     '''
    #     Test code when user narrow down to 0 categorical option
    #     '''
    #     client = get_test_client()
    #     headers = get_token_auth_headers()
    #     json_response = answer_initilization(
    #         client=client,
    #         headers=headers,
    #         survey_update_method=method,
    #         time_period=time,
    #         number_of_copies=number,
    #         max_rounds=rounds,
    #         survey_topics=survey_topics,
    #         mturk_id=mturk_id
    #     )

    #     survey_answer_id = json_response['survey_answer_id']
    #     updated_survey_topics = json_response['updated_survey_topics'] 
    #     for key, val in survey_topics.items():
    #         assert val['answer_type'] == updated_survey_topics[key]['answer_type']
    #         assert val['topic_question'] == updated_survey_topics[key]['topic_question']
    #         assert val['unit'] == updated_survey_topics[key]['unit']

    #     for round in range(1, rounds):
    #         survey_new_answers = select_first_option(updated_survey_topics=updated_survey_topics)
    #         print(f'~~survey_new_answers: {survey_new_answers}')
    #         data = json.dumps({
    #             'survey_answer_id': survey_answer_id,
    #             'survey_new_answers': survey_new_answers,
    #         })

    #         response = client.post(
    #             get_api_url('voter_submit_answers'), 
    #             headers=headers, 
    #             data=data
    #         )
    #         assert response.status_code == 200

    #         json_response = json.loads(response.get_data(as_text=True))
    #         survey_update_method = json_response['survey_update_method']
    #         updated_survey_topics = json_response['updated_survey_topics']
    #         survey_answer_id = json_response['survey_answer_id']
    #         assert len(updated_survey_topics) != {}
    #         print(f'!!updated_survey_topics: {updated_survey_topics}')

    #     # msg = 'cannot input empty survey_new_answers'
    #     # with pytest.raises(ValueError, match=msg):
    #     survey_new_answers = select_first_option(updated_survey_topics=updated_survey_topics)
    #     data = json.dumps({
    #         'survey_answer_id': survey_answer_id,
    #         'survey_new_answers': survey_new_answers,
    #     })
    #     response = client.post(
    #         get_api_url('voter_submit_answers'), 
    #         headers=headers, 
    #         data=data
    #     )
    #     json_response = json.loads(response.get_data(as_text=True))
    #     print('jjj', json_response)
    #     updated_survey_topics = json_response['updated_survey_topics']
    #     # last round, should not update topics
    #     assert updated_survey_topics == {}