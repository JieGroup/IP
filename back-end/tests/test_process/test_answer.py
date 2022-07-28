from __future__ import annotations

import json
import pytest

from app.utils.api import Constant

from app.process.api import (
    SurveyTemplate,
    VoterAnswerSurvey
)

from app.error import DBDocumentNotFound


class TestVoterAnswerSurvey():

    @pytest.mark.parametrize(
        "method, time, number, rounds, survey_topics, mturk_id, expected_survey_topics", 
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
                '123',
                {
                    'age': {
                        'choices_list': [
                            {
                                'min': 0,
                                'max': 80
                            },
                            # {
                            #     'stop': 'stop'
                            # },
                        ]
                    }
                }
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
                '1234',
                {
                    'age': {
                        'choices_list': [
                            {
                                'inclusion': 1,
                            },
                            {
                                'inclusion': 2,
                            },
                            {
                                'inclusion': '3',
                            },
                            {
                                'inclusion': 4,
                            },
                            # {
                            #     'stop': 'stop'
                            # },
                        ]
                    }
                }
            )
        ]
    )
    def test_start_answering_static(self, method, time, number, rounds, survey_topics, mturk_id, expected_survey_topics):
        survey_template_id = SurveyTemplate.create_survey_template(
            survey_update_method=method,
            time_period=time,
            number_of_copies=number,
            max_rounds=rounds,
            survey_topics=survey_topics
        )['survey_template_id']

        res = VoterAnswerSurvey.start_answering(
            survey_template_id=survey_template_id,
            mturk_id=mturk_id
        )

        updated_survey_topics = res['updated_survey_topics'] 
        for key, val in survey_topics.items():
            assert val['answer_type'] == updated_survey_topics[key]['answer_type']
            assert val['topic_question'] == updated_survey_topics[key]['topic_question']
            assert val['unit'] == updated_survey_topics[key]['unit']
            print('shima', expected_survey_topics[key]['choices_list'], updated_survey_topics[key]['choices_list'])
            assert expected_survey_topics[key]['choices_list'] == updated_survey_topics[key]['choices_list']


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
    #                             '3',
    #                             4
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
    # def test_start_answering_uniform(self, method, time, number, rounds, survey_topics, mturk_id):

    #     survey_template_id = SurveyTemplate.create_survey_template(
    #         survey_update_method=method,
    #         time_period=time,
    #         number_of_copies=number,
    #         max_rounds=rounds,
    #         survey_topics=survey_topics
    #     )['survey_template_id']
    #     print('333')
    #     res = VoterAnswerSurvey.start_answering(
    #         survey_template_id=survey_template_id,
    #         mturk_id=mturk_id
    #     )
    #     print('rrrres', res)
    #     updated_survey_topics = res['updated_survey_topics'] 
    #     for key, val in survey_topics.items():
    #         assert val['answer_type'] == updated_survey_topics[key]['answer_type']
    #         assert val['topic_question'] == updated_survey_topics[key]['topic_question']
    #         assert val['unit'] == updated_survey_topics[key]['unit']



    # @pytest.mark.parametrize(
    #     "method, time, number, rounds, survey_topics, mturk_id", 
    #     [
    #         (   
    #             'static',
    #             Constant.TIME_PERIOD_LOWER_LIMIT,
    #             Constant.MAX_NUMBER_OF_COPIES,
    #             Constant.MAX_ROUNDS,
    #             {
    #                 'age': {
    #                     'answer_type': 'continuous',
    #                     'continuous_range': {
    #                         'min': 0,
    #                         'max': 80
    #                     }
    #                 }
    #             }, 
    #             '123'
    #         ),
    #     ]
    # )
    # def test_start_answering_exception(self, method, time, number, rounds, survey_topics, mturk_id):

    #     survey_template_id = SurveyTemplate.create_survey_template(
    #         survey_update_method=method,
    #         time_period=time,
    #         number_of_copies=number,
    #         max_rounds=rounds,
    #         survey_topics=survey_topics
    #     )
    #     msg = 'Cannot find the document'
    #     with pytest.raises(ValueError, match=msg):
    #         VoterAnswerSurvey.start_answering(
    #             survey_template_id='11',
    #             mturk_id=mturk_id
    #         )

    
    
    