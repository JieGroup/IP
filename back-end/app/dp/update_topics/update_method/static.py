from __future__ import annotations

import copy
import random
import numpy as np

from app.utils.api import Constant

from app.dp.update_topics.update_method.base import BaseUpdateMethod

from app.dp.update_topics.update_method.abstract_method import AbstractUpdateMethod

from app.error import TopicNoNeedUpdate

from typeguard import typechecked

from app._typing import (
    Categorical_Option_Type,
    Continuous_Option_Type
)

from typing import (
    Union,
    Any
)

from app._typing import (
    Survey_Topics,
    Survey_Prev_Answers,
    Survey_New_Answers,
    Survey_Update_Method
)


@typechecked
class StaticUpdate(AbstractUpdateMethod, BaseUpdateMethod):
    '''
    When the creator of the survey template chooses 
    StaticUpdate, the voter only needs to answer
    each topic in the survey once.

    Update topics is not needed for static mode.
    No funcion needs to be implemented.

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
        cur_topic_ans: dict[str, Continuous_Option_Type],
    ) -> Union[type[TopicNoNeedUpdate], tuple[Continuous_Option_Type, Continuous_Option_Type]]:
        '''
        Generate a new feasible range for voter
        to choose.

        Parameters
        ----------
        cur_topic_ans : dict[str, Continuous_Option_Type]

        Returns
        -------
        tuple[Continuous_Option_Type, Continuous_Option_Type]
        '''
        print('(((((')
        return cur_topic_ans['min'], cur_topic_ans['max']

    @classmethod
    def generate_topic_new_categorical_range(
        cls,
        topic_info: dict[str, Any],
    ) -> Union[type[TopicNoNeedUpdate], list[Categorical_Option_Type]]:
        '''
        If current round is 1, generate topic new categorical 
        range based on initial categorical range(defined in
        survey template).
        If current round > 1, generate topic new categorical 
        range based on initial categorical range and 
        all previous rounds' categorical answers

        We pick half elements in new_topic_range to form new
        categorical question

        Parameters
        ----------
        topic_info : dict[str, Any]

        Returns
        -------
        list
        '''        
        return copy.deepcopy(topic_info['categorical_range']['inclusion'])

    @classmethod
    def generate_topic_new_range(
        cls,
        cur_rounds_num: int,
        topic_name: str,
        topic_info: dict[str, Any],
        survey_prev_answers: Survey_Prev_Answers,
        cur_topic_ans: Union[dict[str, Constant.CONTINUOUS_RANGE_KEY], dict[str, list[Categorical_Option_Type]]]
    ) -> Union[type[TopicNoNeedUpdate], tuple[Continuous_Option_Type, Continuous_Option_Type], list[Categorical_Option_Type]]:
        '''
        This function will only be executed when the voter answers the
        static survey template for the first time
        '''
        print('))))')
        # hard avoid update topic
        if cur_rounds_num == 1:
            return TopicNoNeedUpdate

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
                topic_info=topic_info,
            )
        else:
            raise ValueError('answer type wrong')
    
    @classmethod
    def update_survey_topics(
        cls,
        survey_update_method: Survey_Update_Method,
        cur_rounds_num: int,
        max_rounds: int,
        survey_topics: Survey_Topics,
        survey_prev_answers: Survey_Prev_Answers,
        survey_new_answers: Survey_New_Answers
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
        survey_topics : Survey_Topics
            The detailed information of each topic
        survey_prev_answers : Survey_Prev_Answers
            Previous answers
        survey_new_answers : Survey_New_Answers
            New answers

        Returns
        -------
        Union[None, dict[str, dict[str, Any]]]
        '''
        print('static')
        return super().update_topics_base_flow(
            survey_update_method=survey_update_method,
            cur_rounds_num=cur_rounds_num,
            max_rounds=max_rounds,
            survey_topics=survey_topics,
            survey_prev_answers=survey_prev_answers,
            survey_new_answers=survey_new_answers,
            update_method_recall=cls.generate_topic_new_range
        )            