from __future__ import annotations

import json
import pytest

from app.dp.update_topics.validate.validate_categorical import ValidateCategoricalAnswer

from app.utils.api import Constant

from app.error import SurveyAnswerError


class TestValidateCategoricalAnswer():

    @pytest.mark.parametrize(
        "range, cur_topic_ans, expected", 
        [
            (['4', '5'], ['4', '5', '6'], False),
            (['4', '5', '6'], ['4', '6'], True),
        ]
    )
    def test_is_cur_topic_ans_valid(self, range, cur_topic_ans, expected):
        
        assert expected == ValidateCategoricalAnswer._ValidateCategoricalAnswer__is_cur_topic_ans_valid(
            range=range,
            cur_topic_ans=cur_topic_ans
        )
    
    @pytest.mark.parametrize(
        "range, cur_topic_ans, expected", 
        [
            (['4', {}], ['4', '5', '6'], False),
            (['4', '5', '6'], [[], '6'], True),
        ]
    )
    def test_is_cur_topic_ans_valid_exception(self, range, cur_topic_ans, expected):
        
        with pytest.raises(TypeError):
            assert expected == ValidateCategoricalAnswer._ValidateCategoricalAnswer__is_cur_topic_ans_valid(
                range=range,
                cur_topic_ans=cur_topic_ans
            )
    
    @pytest.mark.parametrize(
        "topic_name, range_criteria, cur_topic_ans, expected", 
        [
            (
                'test1', 
                {
                    Constant.CATEGORICAL_RANGE_KEY: 
                    {
                        'inclusion': ['4', '5', '6']
                    }
                }, 
                ['4', '5'], 
                None
            ),
            (
                'test2', 
                {
                    Constant.CATEGORICAL_RANGE_KEY: 
                    {
                        'inclusion': [5, 6, 7]
                    }
                }, 
                [5, 6], 
                None
            ),
        ]
    )
    def test_validate_categorical_answer(self, topic_name, range_criteria, cur_topic_ans, expected):
        
        assert expected == ValidateCategoricalAnswer.validate_categorical_answer(
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
                    Constant.CATEGORICAL_RANGE_KEY: 
                    {
                        'inclusion': [5]
                    }
                }, 
                ['4', '5']
            ),
            (
                'test2', 
                {
                    Constant.CATEGORICAL_RANGE_KEY: 
                    {
                        'inclusion': [5]
                    }
                }, 
                [5, 6]
            ),
        ]
    )
    def test_validate_categorical_answer_exception(self, topic_name, range_criteria, cur_topic_ans):
        
        msg = f'{topic_name} answer not in range'
        with pytest.raises(SurveyAnswerError, match=msg):
            ValidateCategoricalAnswer.validate_categorical_answer(
                topic_name=topic_name,
                range_criteria=range_criteria,
                cur_topic_ans=cur_topic_ans
            )
    
