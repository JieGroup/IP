from __future__ import annotations

import random

import numpy as np

from app.utils.api import Constant

from app.dp.update_topics.update_method.base import BaseUpdateMethod

from app.dp.update_topics.update_method.abstract_method import AbstractUpdateMethod

from typeguard import typechecked

from app.error import TopicNoNeedUpdate

from typing import (
    Any,
    Union
)


@typechecked
class UniformUpdate(AbstractUpdateMethod, BaseUpdateMethod):
    '''
    When the creator of the survey template chooses 
    UniformUpdate, the topics of the survey template
    can be reformed with max rounds.

    Attributes
    ----------
    None

    Methods
    -------
    generate_topic_new_range
    update_topics
    '''

    @classmethod
    def generate_topic_new_continuous_range(
        cls,
        cur_topic_ans: dict[str, int],
    ) -> tuple[int, int, int]:
        '''
        Generate a new feasible range for voter
        to choose.

        Parameters
        ----------
        cur_topic_ans : dict[str, int]

        Returns
        -------
        tuple[int, int, int]
        '''
        min_value = cur_topic_ans['min']
        max_value = cur_topic_ans['max']

        # If min_val == max_val, we dont need
        # to update the range more
        if min_value == max_value:
            return TopicNoNeedUpdate

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
    ) -> list:
        '''
        If current round is 1, generate topic new categorical 
        range based on initial categorical range.
        If current round > 1, generate topic new categorical 
        range based on initial categorical range and 
        all previous rounds' categorical answers

        We pick half elements in new_topic_range to form new
        categorical question

        Parameters
        ----------
        cur_rounds_num : list[str]
        topic_name : str
        topic_info : dict[str, Any]
        survey_prev_answers : dict[str, Union[str, Any]]
        cur_topic_ans : Union[dict[str, int], dict[str, set]]

        Returns
        -------
        list
        '''
        prev_inclusion = topic_info['categorical_range']['inclusion']
        prev_exclusion = None
        for prev_rounds_num in range(1, cur_rounds_num):
            prev_rounds_key = f'rounds_{prev_rounds_num}'
            prev_ans = survey_prev_answers[prev_rounds_key][topic_name][Constant.CATEGORICAL_RANGE_KEY]

            if 'inclusion' in prev_ans:
                prev_inclusion = prev_inclusion.intersection(prev_ans['inclusion'])
            elif 'exclusion' in prev_ans:
                prev_exclusion = prev_exclusion.union(prev_ans['exclusion'])

        if 'inclusion' in cur_topic_ans[Constant.CATEGORICAL_RANGE_KEY]:
            inclusion = set(cur_topic_ans[Constant.CATEGORICAL_RANGE_KEY]['inclusion'])
            inclusion = prev_inclusion and inclusion
        elif 'exclusion' in cur_topic_ans[Constant.CATEGORICAL_RANGE_KEY]:
            exclusion = set(cur_topic_ans[Constant.CATEGORICAL_RANGE_KEY]['exclusion'])
            exclusion = prev_exclusion and exclusion

        new_feasible_options = inclusion.difference(exclusion)
        new_feasible_options = list(new_feasible_options)

        if len(new_feasible_options) > 1:
            sample_num = np.ceil(len(new_feasible_options)/2.0).astype(int)
            # half sample to obtain the subset to ask
            new_feasible_options = random.sample(new_feasible_options, sample_num)

        return new_feasible_options

    @classmethod
    def generate_topic_new_range(
        cls,
        cur_rounds_num: int,
        topic_name: str,
        topic_info: dict[str, Any],
        survey_prev_answers: dict[str, Union[str, Any]],
        cur_topic_ans: Union[dict[str, int], dict[str, set]]
    ) -> list:

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
            raise ValueError('answer type wrong')

    @classmethod
    def update_survey_topics(
        cls,
        cur_rounds_num: int,
        max_rounds: int,
        survey_topics: dict[dict[str, Any]],
        survey_prev_answers: dict[str, Union[str, Any]],
        survey_new_answers: dict[dict[str, Any]]
    ) -> Union[None, dict[str, dict[str, Any]]]:
        '''
        Call update_topics_base_flow to handle basic logic.
        Pass generate_topic_new_range to handle the custom 
        logic.

        Parameters
        ----------
        cur_rounds_num : int
            The number of rounds for the voter to answer the current survey
        max_rounds : int
            Defines how many times the topic can be regenerated
        survey_topics : dict
            The detailed information of each topic
        survey_prev_answers : dict or None
            Previous answers
        survey_new_answers : dict
            New answers

        Returns
        -------
        Union[None, dict[str, dict[str, Any]]]
        '''
        return super().update_topics_base_flow(
            cur_rounds_num=cur_rounds_num,
            max_rounds=max_rounds,
            survey_topics=survey_topics,
            survey_prev_answers=survey_prev_answers,
            survey_new_answers=survey_new_answers,
            update_method_recall=cls.generate_topic_new_range
        )