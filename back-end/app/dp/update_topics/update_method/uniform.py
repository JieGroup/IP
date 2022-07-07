from __future__ import annotations

import random

import numpy as np

from app.utils.api import Constant

from app.dp.update_topics.update_method.base import BaseUpdateMethod

from app.dp.update_topics.update_method.abstract_method import AbstractUpdateMethod

from typeguard import typechecked

from app.error import TopicNoNeedUpdate

from app._typing import (
    Categorical_Option_Type,
    Continuous_Option_Type
)

from typing import (
    Any,
    Union
)

from app._typing import (
    Survey_Topics,
    Survey_Prev_Answers,
    Survey_New_Answers
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
    def check_if_voter_willing_to_answer(
        cls,
        cur_topic_ans: dict[str, Any]
    ) -> bool:
        '''
        If 'stop' key in cur_topic_ans,
        it means the voter does not want to answer
        this topic more

        Parameters
        ----------
        cur_topic_ans : dict[str, Any]

        Returns
        -------
        bool
        '''
        if 'stop' in cur_topic_ans:
            return False
        return True


    @classmethod
    def generate_topic_new_continuous_range(
        cls,
        cur_topic_ans: dict[str, Continuous_Option_Type],
    ) -> Union[type[TopicNoNeedUpdate], tuple[Continuous_Option_Type, Continuous_Option_Type, Continuous_Option_Type]]:
        '''
        Generate a new feasible range for voter
        to choose.

        Parameters
        ----------
        cur_topic_ans : dict[str, Continuous_Option_Type]

        Returns
        -------
        tuple[Continuous_Option_Type, Continuous_Option_Type, Continuous_Option_Type]
        '''
        if not cls.check_if_voter_willing_to_answer(
            cur_topic_ans=cur_topic_ans
        ):
            return TopicNoNeedUpdate

        min_value = cur_topic_ans['min']
        max_value = cur_topic_ans['max']

        # If min_val == max_val, we dont need
        # to update the range more
        if min_value >= max_value:
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
        survey_prev_answers: Survey_Prev_Answers,
        cur_topic_ans: Union[dict[str, Constant.CONTINUOUS_RANGE_KEY], dict[str, list[Categorical_Option_Type]]]
    ) -> Union[type[TopicNoNeedUpdate], list]:
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
        cur_rounds_num : list[str]
        topic_name : str
        topic_info : dict[str, Any]
        survey_prev_answers : dict[str, Union[str, Any]]
        cur_topic_ans : Union[dict[str, int], dict[str, set]]

        Returns
        -------
        list
        '''
        if not cls.check_if_voter_willing_to_answer(
            cur_topic_ans=cur_topic_ans
        ):
            return TopicNoNeedUpdate
        
        inclusion = set(topic_info['categorical_range']['inclusion'])
        exclusion = set()
        for prev_rounds_num in range(1, cur_rounds_num):
            prev_rounds_key = f'rounds_{prev_rounds_num}'
            prev_ans = survey_prev_answers[prev_rounds_key][topic_name][Constant.CATEGORICAL_RANGE_KEY]

            if 'inclusion' in prev_ans:
                # inclusion needs intersection to narrow down the range
                inclusion = inclusion.intersection(prev_ans['inclusion'])
            elif 'exclusion' in prev_ans:
                # exclution needs union to extend the range
                exclusion = exclusion.union(prev_ans['exclusion'])

        # combine current answer to inclusion
        if 'inclusion' in cur_topic_ans:
            cur_inclusion = set(cur_topic_ans['inclusion'])
            inclusion = inclusion.intersection(cur_inclusion)
        # combine current answer to exclusion
        elif 'exclusion' in cur_topic_ans:
            cur_exclusion = set(cur_topic_ans['exclusion'])
            exclusion = exclusion.union(cur_exclusion)
            
        # Pick the elements that are in inclusion and not in 
        # exclusion
        new_feasible_options = inclusion.difference(exclusion)
        new_feasible_options = list(new_feasible_options)

        if len(new_feasible_options) < 1:
            return TopicNoNeedUpdate
        elif len(new_feasible_options) >= 1:
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
        survey_prev_answers: Survey_Prev_Answers,
        cur_topic_ans: Union[dict[str, Constant.CONTINUOUS_RANGE_KEY], dict[str, list[Categorical_Option_Type]]]
    ) -> Union[type[TopicNoNeedUpdate], tuple[Continuous_Option_Type, Continuous_Option_Type, Continuous_Option_Type], list]:

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
        return super().update_topics_base_flow(
            cur_rounds_num=cur_rounds_num,
            max_rounds=max_rounds,
            survey_topics=survey_topics,
            survey_prev_answers=survey_prev_answers,
            survey_new_answers=survey_new_answers,
            update_method_recall=cls.generate_topic_new_range
        )