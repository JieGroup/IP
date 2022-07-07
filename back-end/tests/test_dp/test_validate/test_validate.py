from __future__ import annotations

import pytest

from app.dp.update_topics.validate.validate import ValidateAnswer

from app.utils.api import Constant

from app.error import SurveyAnswerError


class TestValidateAnswer():

    @pytest.mark.parametrize(
        "cur_rounds_num, expected",
        [
            (1, True),
            (2, False)
        ]
    )
    def test_is_cur_topic_ans_valid(self, cur_rounds_num, expected):
        
        assert expected == ValidateAnswer._ValidateAnswer__is_cur_rounds_num_equals_one(
            cur_rounds_num=cur_rounds_num,
        )
    
    @pytest.mark.parametrize(
        "cur_rounds_num, topic_name, topic_info, survey_prev_answers, expected", 
        [
            (
                1,
                'test1', 
                {   
                    Constant.CONTINUOUS_RANGE_KEY:
                    {
                        'min': 555,
                        'max': 666
                    }
                },
                {}, 
                {   
                    Constant.CONTINUOUS_RANGE_KEY:
                    {
                        'min': 555,
                        'max': 666
                    }
                },
            ),
            (
                2,
                'test1', 
                {   
                    Constant.CONTINUOUS_RANGE_KEY:
                    {
                        'min': 555,
                        'max': 666
                    }
                    
                },
                {   
                    'rounds_1': 
                    {
                        'test1':
                        {
                            Constant.CONTINUOUS_RANGE_KEY: 
                            {
                                'min': 4,
                                'max': 10
                            }
                        }
                    } 
                }, 
                {
                    Constant.CONTINUOUS_RANGE_KEY: 
                    {
                        'min': 4,
                        'max': 10
                    }
                }
            ),
        ]
    )
    def test_get_range_criteria(self, cur_rounds_num, topic_name, topic_info, survey_prev_answers, expected):
        
        assert expected == ValidateAnswer._ValidateAnswer__get_range_criteria(
            cur_rounds_num=cur_rounds_num,
            topic_name=topic_name,
            topic_info=topic_info,
            survey_prev_answers=survey_prev_answers
        )

    @pytest.mark.parametrize(
        "cur_rounds_num, survey_topics, survey_prev_answers, survey_new_answers, expected", 
        [
            (
                1, 
                {   
                    'test1':
                    {
                        'answer_type': 'continuous',
                        Constant.CONTINUOUS_RANGE_KEY:
                        {
                            'min': 555,
                            'max': 666
                        }
                    }
                },
                {}, 
                {   
                    'test1':
                    {
                        Constant.CONTINUOUS_RANGE_KEY:
                        {
                            'min': 600,
                            'max': 666
                        }
                    }
                },
                None
            ),
            (
                2, 
                {   
                    'test1':
                    {   
                        'answer_type': 'continuous',
                        Constant.CONTINUOUS_RANGE_KEY:
                        {
                            'min': 555,
                            'max': 666
                        }
                    }
                },
                {   
                    'rounds_1': 
                    {
                        'test1':
                        {
                            Constant.CONTINUOUS_RANGE_KEY: 
                            {
                                'min': 600,
                                'max': 666,
                            }
                        }
                    } 
                },  
                {   
                    'test1':
                    {
                        Constant.CONTINUOUS_RANGE_KEY:
                        {
                            'min': 650,
                            'max': 666
                        }
                    }
                },
                None
            ),
        ]
    )
    def test_validate_survey_answers(self, cur_rounds_num, survey_topics, survey_prev_answers, survey_new_answers, expected):
        
        assert expected == ValidateAnswer.validate_survey_answers(
                cur_rounds_num=cur_rounds_num,
                survey_topics=survey_topics,
                survey_prev_answers=survey_prev_answers,
                survey_new_answers=survey_new_answers
            )
    

    @pytest.mark.parametrize(
        "cur_rounds_num, survey_topics, survey_prev_answers, survey_new_answers, expected", 
        [
            (
                1, 
                {   
                    'test1':
                    {
                        'answer_type': 'continuous',
                        Constant.CONTINUOUS_RANGE_KEY:
                        {
                            'min': 555,
                            'max': 666
                        }
                    }
                },
                {}, 
                {   
                    'test2':
                    {
                        Constant.CONTINUOUS_RANGE_KEY:
                        {
                            'min': 600,
                            'max': 666
                        }
                    }
                },
                'test1'
            ),
            (
                2, 
                {   
                    'test3':
                    {
                        'answer_type': 'continuous',
                        Constant.CONTINUOUS_RANGE_KEY:
                        {
                            'min': 555,
                            'max': 666
                        }
                    }
                },
                {}, 
                {   
                    'test2':
                    {
                        Constant.CONTINUOUS_RANGE_KEY:
                        {
                            'min': 600,
                            'max': 666
                        }
                    }
                },
                'test3'
            ),
        ]
    )
    def test_validate_survey_answers_SurveyAnswerError_exception(self, cur_rounds_num, survey_topics, survey_prev_answers, survey_new_answers, expected):
        
        msg = f'Missing {expected} in survey_new_answers'
        with pytest.raises(SurveyAnswerError, match=msg):
            assert expected == ValidateAnswer.validate_survey_answers(
                    cur_rounds_num=cur_rounds_num,
                    survey_topics=survey_topics,
                    survey_prev_answers=survey_prev_answers,
                    survey_new_answers=survey_new_answers
                )