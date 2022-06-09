from __future__ import annotations
from ctypes import Union

import sys
import uuid
import random
import string
import numpy as np

from random import Random
from flask import session

from app import database, pyMongo
from app.utils.constant import Constant
from app.database import select_mongoDB_operator

from app.error import SurveyAnswerError

from typing import (
    Any,
    final
)


class ValidateBase:
    @final
    @classmethod
    def placeholder(cls):
        pass


class ValidateCategoricalAnswer(ValidateBase):

    @classmethod
    def validate_categorical_answer(
        cls,
        # TODO: 标注radiofield到底是什么
        answer_range: Union[Any, str],
        cur_topic_ans: str
    ) -> None:

        answer_range = decode_continuous_range_str_to_int(answer_range)
        cur_topic_ans = decode_continuous_range_str_to_int(cur_topic_ans)

        if not cls.if_cur_topic_ans_valid(
            answer_range=answer_range,
            cur_topic_ans=cur_topic_ans
        ):
            raise SurveyAnswerError
            
        return


class ValidateContinuousAnswer(ValidateBase):

    @classmethod
    def if_cur_topic_ans_valid(
        cls,
        answer_range: list[int],
        cur_topic_ans: list[int],
    ) -> bool:

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
    def decode_continuous_range_str_to_int(
        continuous_range: str
    ) -> list[int]:

        continuous_range_list = continuous_range.split('-')

        for i in range(len(continuous_range_list)):
            continuous_range_list[i] = int(continuous_range_list.strip())

        return continuous_range_list

    @classmethod
    def validate_continuous_answer(
        cls,
        # TODO: 标注radiofield到底是什么
        # answer_range: Union[Any, str],
        # cur_topic_ans: str

        cur_rounds_num: int,
        topic_name: str,
        topic_info: dict[str, Any],
        prev_answer: Union[None, dict[str, dict[str, Any]]],
        cur_topic_ans: dict[str, int],
    ) -> None:

        answer_range = prev_answer['continuous_range']
        
        if not cls.if_cur_topic_ans_valid(
            answer_range=answer_range,
            cur_topic_ans=cur_topic_ans
        ):
            raise SurveyAnswerError

        return


