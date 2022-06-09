from __future__ import annotations
from os import setegid

import random
import collections

from torch import R

from app import pyMongo
from app.database.database.utils import (
    if_file_size_exceed_limit
)

from app.dp.update_topics.update_method.utils import(
    CATEGORICAL_RANGE_KEY,
    CONTINUOUS_RANGE_KEY
)

from app.dp.update_topics.update_method.base import BaseUpdateMethod

from app.dp.update_topics.update_method.abstract_method import AbstractUpdateMethod

from typing import (
    Any,
    Union
)

class UniformUpdate(AbstractUpdateMethod, BaseUpdateMethod):

    @classmethod
    def generate_topic_new_continuous_range(
        cls,
        cur_topic_ans: dict[str, int],
    ) -> tuple[int, int, int]:

        '''
            1. Check the validity of cur_topic_ans
            2. Generate new continuous range
        '''
        
        #TODO: 如果min max相等怎么办
        min_value = cur_topic_ans['min']
        max_value = cur_topic_ans['max']

        # Generate new_mid_value from min_value to max_value-1
        # to avoid max_value overflow
        new_mid_value = random.randint(min_value, max_value-1)
        return min_value, new_mid_value, max_value

    @classmethod
    def generate_topic_new_categorical_range(
        cls,
        cur_rounds_num: int,
        topic_name: str,
        topic_info: dict[str, Any],
        survey_prev_answers: dict[str, Union[str, Any]],
        cur_topic_ans: Union[dict[str, int], dict[str, set]]
    ) -> None:

        '''
            If current round is 1, generate topic new categorical 
            range based on initial categorical range.
            If current round > 1, generate topic new categorical 
            range based on initial categorical range and 
            all previous rounds' categorical answers
        '''

        prev_inclusion = topic_info['categorical_range']['inclusion']
        prev_exclusion = None
        for prev_rounds_num in range(1, cur_rounds_num):
            prev_rounds_key = f'rounds_{prev_rounds_num}'
            prev_ans = survey_prev_answers[prev_rounds_key][topic_name][CATEGORICAL_RANGE_KEY]

            if 'inclusion' in prev_ans:
                prev_inclusion = prev_inclusion.intersection(prev_ans['inclusion'])
            elif 'exclusion' in prev_ans:
                prev_exclusion = prev_exclusion.union(prev_ans['exclusion'])

        if 'inclusion' in cur_topic_ans[CATEGORICAL_RANGE_KEY]:
            inclusion = set(cur_topic_ans[CATEGORICAL_RANGE_KEY]['inclusion'])
            inclusion = prev_inclusion and inclusion
        elif 'exclusion' in cur_topic_ans[CATEGORICAL_RANGE_KEY]:
            exclusion = set(cur_topic_ans[CATEGORICAL_RANGE_KEY]['exclusion'])
            exclusion = prev_exclusion and exclusion

        new_feasible_options = inclusion.difference(exclusion)

        return new_feasible_options

    @classmethod
    def generate_topic_new_range(
        cls,
        cur_rounds_num: int,
        topic_name: str,
        topic_info: dict[str, Any],
        survey_prev_answers: dict[str, Union[str, Any]],
        cur_topic_ans: Union[dict[str, int], dict[str, set]]
    ):

        answer_type = topic_info['answer_type']
        if answer_type == 'continuous':
            return cls.generate_topic_new_continuous_range(
                cur_topic_ans=cur_topic_ans
            )
        # If answer_type is categorical, then we need to 
        # use initial answer range and previous answers
        # to generate new question.
        elif answer_type == 'categorical':
            return cls.generate_topic_new_categorical_range(
                cur_rounds_num=cur_rounds_num,
                topic_name=topic_name,
                topic_info=topic_info,
                survey_prev_answers=survey_prev_answers,
                cur_topic_ans=cur_topic_ans
            )
        else:
            # TODO: Error
            return None


    @classmethod
    def update_survey_topics(
        cls,
        cur_rounds_num: int,
        max_rounds: int,
        survey_topics: dict[dict[str, Any]],
        survey_prev_answers: dict[str, Union[str, Any]],
        survey_new_answers: dict[dict[str, Any]]
    ) -> None:

        # 先检查answer
        # 再生成新的topics

        # 现在的问题是我在生成新的topics的时候检查answer，感觉耦合在了一起。分不开的
        # 原因是检查answer需要topic

        '''
            1. check current rounds of answering survey
            1. check survey_answers
            2. Update survey_topics if needed
        '''

        return super().update_topics_base_flow(
            cur_rounds_num=cur_rounds_num,
            max_rounds=max_rounds,
            survey_topics=survey_topics,
            survey_prev_answers=survey_prev_answers,
            survey_new_answers=survey_new_answers,
            update_method_recall=cls.generate_topic_new_range
        )