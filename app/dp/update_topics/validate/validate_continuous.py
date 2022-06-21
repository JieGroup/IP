from __future__ import annotations

from typeguard import typechecked

from app.utils.api import Constant

from app.error import SurveyAnswerError

from app.dp.update_topics.validate.base import ValidateBase

from typing import Any

from app._typing import Continuous_Option_Type


@typechecked
class ValidateContinuousAnswer(ValidateBase):
    '''
    Validate new continuous answer

    Attributes
    ----------
    None

    Methods
    -------
    validate_continuous_answer
    '''

    @classmethod
    def __is_cur_topic_ans_valid(
        cls,
        min_val: Continuous_Option_Type,
        max_val: Continuous_Option_Type,
        cur_topic_ans: dict[str, Continuous_Option_Type],
    ) -> bool:
        '''
        Check if cur_topic_ans(continuous) is 
        in range
        
        Parameters
        ----------
        range : dict[str, int]
        cur_topic_ans : dict[str, int]

        Returns
        -------
        bool
        '''
        # cur_topic_ans should only contains min value and max value
        if len(cur_topic_ans) != 2:
            return False

        # check min value
        if cur_topic_ans['min'] < min_val:
            return False
        
        # check max value
        if cur_topic_ans['max'] > max_val:
            return False

        return True

    @classmethod
    def validate_continuous_answer(
        cls,
        topic_name: str,
        range_criteria: dict[str, Any],
        cur_topic_ans: dict[str, Continuous_Option_Type],
    ) -> None:
        '''
        Check if cur_topic_ans is in answer_range
        
        Parameters
        ----------
        topic_name : str
        range_criteria : dict[str, Any]
        cur_topic_ans : str

        Returns
        -------
        None
        '''
        if not cls.__is_cur_topic_ans_valid(
            min_val=range_criteria[Constant.CONTINUOUS_RANGE_KEY]['min'],
            max_val=range_criteria[Constant.CONTINUOUS_RANGE_KEY]['max'],
            cur_topic_ans=cur_topic_ans
        ):
            raise SurveyAnswerError(f'{topic_name} answer not in range')

        return