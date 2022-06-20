from __future__ import annotations

from app.error import SurveyAnswerError

from typeguard import typechecked

from app.utils.api import Constant

from typing import (
    Any,
    final,
    Union
)


@typechecked
class ValidateBase:
    @final
    @classmethod
    def placeholder(cls):
        pass


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
        answer_range: dict[str, int],
        cur_topic_ans: dict[str, int],
    ) -> bool:
        '''
        Check if cur_topic_ans is in answer_range
        
        Parameters
        ----------
        answer_range : dict[str, int]
        cur_topic_ans : dict[str, int]

        Returns
        -------
        bool
        '''
        return cur_topic_ans in set(answer_range)


    @classmethod
    def validate_categorical_answer(
        cls,
        topic_name: str,
        prev_answer: Union[Any, str],
        cur_topic_ans: str
    ) -> None:
        '''
        Check if cur_topic_ans is in answer_range
        
        Parameters
        ----------
        topic_name : str
        answer_range : list[str]
        cur_topic_ans : str

        Returns
        -------
        None
        '''
        if not cls.__is_cur_topic_ans_valid(
            answer_range=prev_answer[Constant.CATEGORICAL_RANGE_KEY],
            cur_topic_ans=cur_topic_ans
        ):
            raise SurveyAnswerError(f'{topic_name} answer not in range')
            
        return

@typechecked
class ValidateContinuousAnswer(ValidateBase):

    @classmethod
    def __is_cur_topic_ans_valid(
        cls,
        answer_range: dict[str, int],
        cur_topic_ans: dict[str, int],
    ) -> bool:
        '''
        Check if cur_topic_ans is in answer_range
        
        Parameters
        ----------
        answer_range : dict[str, int]
        cur_topic_ans : dict[str, int]

        Returns
        -------
        bool
        '''
        # cur_topic_ans should only contains min value and max value
        if len(cur_topic_ans) != 2:
            return False

        # check min value
        if cur_topic_ans['min'] < answer_range['min']:
            return False
        
        # check max value
        if cur_topic_ans['max'] > answer_range['max']:
            return False

        return True

    @classmethod
    def validate_continuous_answer(
        cls,
        topic_name: str,
        prev_answer: Union[None, dict[str, dict[str, Any]]],
        cur_topic_ans: dict[str, int],
    ) -> None:
        '''
        Check if cur_topic_ans is in answer_range
        
        Parameters
        ----------
        topic_name : str
        answer_range : list[str]
        cur_topic_ans : str

        Returns
        -------
        None
        '''
        if not cls.__is_cur_topic_ans_valid(
            answer_range=prev_answer[Constant.CONTINUOUS_RANGE_KEY],
            cur_topic_ans=cur_topic_ans
        ):
            raise SurveyAnswerError(f'{topic_name} answer not in range')

        return

    # @classmethod
    # def decode_continuous_range_str_to_int(
    #     continuous_range: str
    # ) -> list[int]:

    #     continuous_range_list = continuous_range.split('-')

    #     for i in range(len(continuous_range_list)):
    #         continuous_range_list[i] = int(continuous_range_list.strip())

    #     return continuous_range_list

