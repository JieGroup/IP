from __future__ import annotations

import pytest

from app.dp.update_topics.validate.validate_continuous import ValidateContinuousAnswer

from app.utils.api import Constant

from app.error import SurveyAnswerError


class TestValidateContinuousAnswer():

    @pytest.mark.parametrize(
        "min_val, max_val, cur_topic_ans, expected", 
        [
            (
                4, 
                10, 
                {
                    'min': 3,
                    'max': 7
                },
                False
            ),
            (
                4, 
                10, 
                {
                    'min': 4,
                    'max': 7
                },
                True
            ),
        ]
    )
    def test_is_cur_topic_ans_valid(self, min_val, max_val, cur_topic_ans, expected):
        
        assert expected == ValidateContinuousAnswer._ValidateContinuousAnswer__is_cur_topic_ans_valid(
            min_val=min_val,
            max_val=max_val,
            cur_topic_ans=cur_topic_ans
        )
    
    @pytest.mark.parametrize(
        "topic_name, range_criteria, cur_topic_ans, expected", 
        [
            (
                'test1', 
                {
                    Constant.CONTINUOUS_RANGE_KEY: 
                    {
                        'min': 4,
                        'max': 10
                    }
                }, 
                {
                    'min': 4,
                    'max': 10
                },
                None
            ),
            (
                'test2', 
                {
                    Constant.CONTINUOUS_RANGE_KEY: 
                    {
                        'min': 4,
                        'max': 10
                    }
                }, 
                {
                    'min': 6,
                    'max': 8
                },
                None
            ),
        ]
    )
    def test_validate_continuous_answer(self, topic_name, range_criteria, cur_topic_ans, expected):
        
        assert expected == ValidateContinuousAnswer.validate_continuous_answer(
            topic_name=topic_name,
            range_criteria=range_criteria,
            cur_topic_ans=cur_topic_ans
        )

    @pytest.mark.parametrize(
        "topic_name, range_criteria, cur_topic_ans", 
        [
            (
                'test1', 
                {
                    Constant.CONTINUOUS_RANGE_KEY: 
                    {
                        'min': 5,
                        'max': 10
                    }
                }, 
                {
                    'min': 4,
                    'max': 10
                }
            ),
            (
                'test2', 
                {
                    Constant.CONTINUOUS_RANGE_KEY: 
                    {
                        'min': 8,
                        'max': 10
                    }
                }, 
                {
                    'min': 6,
                    'max': 8
                }
            ),
        ]
    )
    def test_validate_continuous_answer_exception(self, topic_name, range_criteria, cur_topic_ans):
        
        msg = f'{topic_name} answer not in range'
        with pytest.raises(SurveyAnswerError, match=msg):
            ValidateContinuousAnswer.validate_continuous_answer(
                topic_name=topic_name,
                range_criteria=range_criteria,
                cur_topic_ans=cur_topic_ans
            )
    
