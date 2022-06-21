from __future__ import annotations

import pytest

from tests.test_dp.test_update_method.conftest import UniformUpdate

from app.utils.api import Constant

from app.error import TopicNoNeedUpdate


class TestUniformUpdate():

    @pytest.mark.usefixtures('UniformUpdate')
    @pytest.mark.parametrize(
        "cur_topic_ans", 
        [
            {
                'min': 20,
                'max': 50
            },   
        ]
    )
    def test_generate_topic_new_continuous_range(self, UniformUpdate, cur_topic_ans):
        
        res = UniformUpdate.generate_topic_new_continuous_range(
            cur_topic_ans=cur_topic_ans
        )
        assert res[0] <= res[1] <= res[2]
        return 
    
    @pytest.mark.usefixtures('UniformUpdate')
    @pytest.mark.parametrize(
        "cur_topic_ans, expected", 
        [
            (
                {
                    'min': 50,
                    'max': 50
                },
                TopicNoNeedUpdate
            ),   
            (   
                {
                    'stop': True
                },
                TopicNoNeedUpdate
            )
        ]
    )
    def test_generate_topic_new_continuous_range_exception(self, UniformUpdate, cur_topic_ans, expected):
        
        assert expected == UniformUpdate.generate_topic_new_continuous_range(
            cur_topic_ans=cur_topic_ans
        )

    @pytest.mark.usefixtures('UniformUpdate')
    @pytest.mark.parametrize(
        "rounds, name, info, prev_answers, cur_topic_ans, expected, expected_length", 
        [
            (
                1, 
                'test1',
                {
                    Constant.CATEGORICAL_RANGE_KEY: 
                    {
                        'inclusion': ['5', '6', '7']
                    }
                },
                {},
                {
                    Constant.CATEGORICAL_RANGE_KEY: 
                    {
                        'inclusion': ['5', '6']
                    }
                },
                {
                    '5',
                    '6'
                },
                1
            ),
            (
                3, 
                'test1',
                {
                    Constant.CATEGORICAL_RANGE_KEY: 
                    {
                        'inclusion': [str(i) for i in range(10)]
                    }
                },
                {
                    'rounds_1': 
                    {
                        'test1':
                        {
                            Constant.CATEGORICAL_RANGE_KEY: 
                            {
                                'exclusion': [str(i) for i in range(5)]
                            }
                        }
                    },
                    'rounds_2': 
                    {
                        'test1':
                        {
                            Constant.CATEGORICAL_RANGE_KEY: 
                            {
                                'exclusion': ['5', '6', '7']
                            }
                        }
                    },
                },
                {
                    Constant.CATEGORICAL_RANGE_KEY: 
                    {
                        'exclusion': ['8']
                    }
                },
                {
                    '9'
                },
                1
            )      
        ]
    )
    def test_generate_topic_new_categorical_range(self, UniformUpdate, rounds, name, info, prev_answers, cur_topic_ans, expected, expected_length):
        
        res = UniformUpdate.generate_topic_new_categorical_range(
            cur_rounds_num=rounds,
            topic_name=name,
            topic_info=info,
            survey_prev_answers=prev_answers,
            cur_topic_ans=cur_topic_ans
        )
        
        assert set(res).issubset(set(expected))
        assert len(res) == expected_length
    
    # @pytest.mark.usefixtures('UniformUpdate')
    # @pytest.mark.parametrize(
    #     "rounds, name, info, prev_answers, cur_topic_ans, expected", 
    #     [ 
    #         (   
    #             {
    #                 'stop': True
    #             },
    #             TopicNoNeedUpdate
    #         )
    #     ]
    # )
    # def test_generate_topic_new_categorical_range_exception(self, UniformUpdate, cur_topic_ans, expected):
        
    #     assert expected == UniformUpdate.generate_topic_new_categorical_range(
    #         cur_topic_ans=cur_topic_ans
    #     )