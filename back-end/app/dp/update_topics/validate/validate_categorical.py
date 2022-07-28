from __future__ import annotations

from typeguard import typechecked

from app.utils.api import Constant

from app.error import SurveyAnswerError

from app.dp.update_topics.validate.base import ValidateBase

from typing import (
    Any,
    Union
)

from app._typing import Categorical_Option_Type


@typechecked
class ValidateCategoricalAnswer(ValidateBase):
    '''
    Validate new categorical answer

    Attributes
    ----------
    None

    Methods
    -------
    validate_categorical_answer
    '''

    @classmethod
    def __is_cur_topic_ans_valid(
        cls,
        range: list[Categorical_Option_Type],
        cur_topic_ans: Union[Categorical_Option_Type, list[Categorical_Option_Type]],
    ) -> bool:
        '''
        Check if cur_topic_ans(categorical) is 
        in range
        
        Parameters
        ----------
        range : dict[str, int]
        cur_topic_ans : str

        Returns
        -------
        bool
        '''
        print('range', range)
        print('cur_topic_ans', cur_topic_ans, set(cur_topic_ans), set(cur_topic_ans).issubset(range))
        return set(cur_topic_ans).issubset(range)


    @classmethod
    def validate_categorical_answer(
        cls,
        topic_name: str,
        range_criteria: dict[str, Any],
        cur_topic_ans: dict[str, Union[Categorical_Option_Type, list[Categorical_Option_Type]]]
    ) -> None:
        '''
        Check if cur_topic_ans is in answer_range
        
        Parameters
        ----------
        topic_name : str
        range_criteria : dict[str, Any]
        cur_topic_ans : list[Categorical_Option_Type]

        Returns
        -------
        None
        '''
        if 'inclusion' in cur_topic_ans:
            cur_topic_ans = cur_topic_ans['inclusion']
        elif 'exclusion' in cur_topic_ans:
            cur_topic_ans = cur_topic_ans['exclution']
            
        if not cls.__is_cur_topic_ans_valid(
            range=range_criteria[Constant.CATEGORICAL_RANGE_KEY]['inclusion'],
            cur_topic_ans=cur_topic_ans
        ):
            raise SurveyAnswerError(f'{topic_name} answer not in range')
            
        return
