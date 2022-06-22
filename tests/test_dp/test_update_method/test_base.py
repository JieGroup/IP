from __future__ import annotations
from curses import reset_prog_mode

import pytest

from app.dp.update_topics.update_method.base import BaseUpdateMethod

from app.dp.update_topics.update_method.api import GetUniformUpdate

from app.utils.api import Constant

from app.error import TopicNoNeedUpdate


class TestBaseUpdateMethod():
    
    @pytest.mark.parametrize(
        "cur_rounds_num, max_rounds_of_survey, expected", 
        [
            (-5, 6, False),
            (1, 8, True),
            (6, 5, False)  
        ]
    )
    def test_is_cur_rounds_num_valid(self, cur_rounds_num, max_rounds_of_survey, expected):
        
        assert expected == BaseUpdateMethod._BaseUpdateMethod__is_cur_rounds_num_valid(
            cur_rounds_num=cur_rounds_num,
            max_rounds_of_survey=max_rounds_of_survey
        )

    @pytest.mark.parametrize(
        "cur_rounds_num, max_rounds_of_survey, expected", 
        [
            (-5, 6, False),
            (1, 8, True),
            (5, 5, False),
            (4, 5, True)  
        ]
    )
    def test_if_survey_topics_need_updating(self, cur_rounds_num, max_rounds_of_survey, expected):
        
        assert expected == BaseUpdateMethod._BaseUpdateMethod__if_survey_topics_need_updating(
            cur_rounds_num=cur_rounds_num,
            max_rounds_of_survey=max_rounds_of_survey
        )
    

    @pytest.mark.parametrize(
        "rounds, max_rounds, survey_topics, survey_prev_answers, survey_new_answers, recall, expected", 
        [
            (
                2,
                3,
                {   
                    'test_key_1':
                    {
                        'answer_type': 'categorical',
                        Constant.CATEGORICAL_RANGE_KEY: 
                        {
                            'inclusion': [str(i) for i in range(10)]
                        }
                    }
                },
                {
                    'rounds_1': 
                    {
                        'test_key_1':
                        {
                            Constant.CATEGORICAL_RANGE_KEY: 
                            {
                                'exclusion': [str(i) for i in range(5)]
                            }
                        }
                    },
                },
                {   
                    'test_key_1':
                    {
                        Constant.CATEGORICAL_RANGE_KEY: 
                        {
                            'exclusion': ['5', '6', '7']
                        }
                    }
                },
                GetUniformUpdate.get_class().generate_topic_new_range,
                {
                    'test_key_1':
                    {   
                        'answer_type': 'categorical',
                        'choices_list': 
                        [
                            {'8', '9'},
                            'exclusion',
                            'stop'
                        ]
                    }
                }
            )              
        ]
    )
    def test_categorical_update_topics_base_flow(self, rounds, max_rounds, survey_topics, survey_prev_answers, survey_new_answers, recall, expected):
        
        res = BaseUpdateMethod.update_topics_base_flow(
            cur_rounds_num=rounds, 
            max_rounds=max_rounds,
            survey_topics=survey_topics,
            survey_prev_answers=survey_prev_answers,
            survey_new_answers=survey_new_answers,
            update_method_recall=recall
        )

        for key in res.keys():
            res_val = res[key]
            expected_val = expected[key]

            answer_type = res_val['answer_type']
            choices_list = res_val['choices_list']

            assert answer_type == expected_val['answer_type']
            assert set(choices_list[0]).issubset(set(expected_val['choices_list'][0]))
            assert choices_list[1] == expected_val['choices_list'][1]
            assert choices_list[2] == expected_val['choices_list'][2]


    @pytest.mark.parametrize(
        "rounds, max_rounds, survey_topics, survey_prev_answers, survey_new_answers, recall, expected", 
        [
            (
                2,
                3,
                {   
                    'test_key_1':
                    {
                        'answer_type': 'categorical',
                        Constant.CATEGORICAL_RANGE_KEY: 
                        {
                            'inclusion': [str(i) for i in range(10)]
                        }
                    }
                },
                {
                    'rounds_1': 
                    {
                        'test_key_1':
                        {
                            Constant.CATEGORICAL_RANGE_KEY: 
                            {
                                'exclusion': [str(i) for i in range(5)]
                            }
                        }
                    },
                },
                {   
                    'test_key_1':
                    {
                        Constant.CATEGORICAL_RANGE_KEY: 
                        {
                            'exclusion': ['5', '6', '7', '8', '9']
                        }
                    }
                },
                GetUniformUpdate.get_class().generate_topic_new_range,
                {}
            ),
            (
                2,
                3,
                {   
                    'test_key_1':
                    {
                        'answer_type': 'categorical',
                        Constant.CATEGORICAL_RANGE_KEY: 
                        {
                            'inclusion': [str(i) for i in range(10)]
                        }
                    }
                },
                {
                    'rounds_1': 
                    {
                        'test_key_1':
                        {
                            Constant.CATEGORICAL_RANGE_KEY: 
                            {
                                'exclusion': [str(i) for i in range(5)]
                            }
                        }
                    },
                },
                {   
                    'test_key_2':
                    {
                        Constant.CATEGORICAL_RANGE_KEY: 
                        {
                            'exclusion': ['5', '6', '7', '8', '9']
                        }
                    }
                },
                GetUniformUpdate.get_class().generate_topic_new_range,
                {}
            )                         
        ]
    )
    def test_categorical_update_topics_base_flow(self, rounds, max_rounds, survey_topics, survey_prev_answers, survey_new_answers, recall, expected):
        
        assert expected == BaseUpdateMethod.update_topics_base_flow(
            cur_rounds_num=rounds, 
            max_rounds=max_rounds,
            survey_topics=survey_topics,
            survey_prev_answers=survey_prev_answers,
            survey_new_answers=survey_new_answers,
            update_method_recall=recall
        )