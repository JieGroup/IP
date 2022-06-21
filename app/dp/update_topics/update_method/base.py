from __future__ import annotations

import collections

from typeguard import typechecked

from app.dp.update_topics.update_method.choices import (
    ReformatCategoricalTopic,
    ReformatContinuousTopic,
)

from app.error import TopicNoNeedUpdate

from app._typing import (
    Answer_Type,
    Survey_Topics,
    Survey_Prev_Answers,
    Survey_New_Answers
)

from typing import (
    final,
    Any,
    Callable,
    Union
)


@typechecked
class BaseUpdateMethod:
    '''
    Base class for database

    Attributes
    ----------
    None

    Methods
    -------
    update_topics_base_flow
    '''

    @final
    def placeholder(self):
        pass

    @final
    @classmethod
    def __is_cur_rounds_num_valid(
        cls,
        cur_rounds_num: int,
        max_rounds_of_survey: int
    ) -> bool:
        '''
        Check if cur_rounds_num is valid

        Parameters
        ----------
        cur_rounds_num : int
            current round number
        max_rounds_of_survey : int
            max round of all topics that can be 
            answered of this survey template

        Returns
        -------
        bool
        '''
        if 1 <= cur_rounds_num <= max_rounds_of_survey:
            return True
        return False
    
    @final
    @classmethod
    def __if_survey_topics_need_updating(
        cls,
        cur_rounds_num: int,
        max_rounds_of_survey: int
    ) -> bool:
        '''
        Check if survey_topics need updating

        Parameters
        ----------
        cur_rounds_num : int
            current round number
        max_rounds_of_survey : int
            max round of all topics that can be 
            answered of this survey template

        Returns
        -------
        bool
        '''
        if 1 <= cur_rounds_num < max_rounds_of_survey:
            return True
        return False
    
    @final
    @classmethod
    def __is_cur_rounds_num_equals_one(
        cls, cur_rounds_num: int
    ) -> bool:
        '''
        Check if cur_rounds_num is one

        Parameters
        ----------
        cur_rounds_num : int
            current round number

        Returns
        -------
        bool
        '''
        return cur_rounds_num == 1
    
    @final
    @classmethod
    def __reformat_topic(
        cls,
        answer_type: Answer_Type,
        topic_new_range: Union[list[str], tuple[int, int, int]] # first type for categorical, second for continuous
    ) -> list[dict, str]:
        '''
        Turn the updated topics to choices that
        can be parsed by the front-end.

        Parameters
        ----------
        answer_type : Answer_Type
        topic_new_range : Union[list[str], tuple[int, int, int]]
            updated topic     

        Returns
        -------
        list[dict, str]
        '''
        if answer_type == 'categorical':
            return ReformatCategoricalTopic.reformat(
                topic_new_range=topic_new_range
            )
        elif answer_type == 'continuous':
            return ReformatContinuousTopic.reformat(
                topic_new_range=topic_new_range
            )

   
    @final
    @classmethod
    def update_topics_base_flow(
        cls,
        cur_rounds_num: int, 
        max_rounds: int,
        survey_topics: Survey_Topics,
        survey_prev_answers: Survey_Prev_Answers,
        survey_new_answers: Survey_New_Answers,
        update_method_recall: Callable
    ) -> Union[None, dict[str, dict[str, Any]]]: # Topics new ranges
        '''
        Abstracting out common workflows that every update method 
        needs to go through 

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
        update_method_recall :
            Callback method to handle each specific method   

        Returns
        -------
        dict
        '''
        # Check if cur_rounds_num <= max_rounds_num
        if not cls.__is_cur_rounds_num_valid(
            cur_rounds_num=cur_rounds_num,
            max_rounds=max_rounds
        ):
            return None
                
        # Check if cur_rounds_num < max_rounds_num
        # If it is, we need to update the question
        if not cls.__if_survey_topics_need_updating(
            cur_rounds_num=cur_rounds_num,
            max_rounds=max_rounds
        ):
            return None

        updated_survey_topics = collections.defaultdict(dict)
        for topic_name, topic_info in survey_topics.items(): 

            if topic_name not in survey_new_answers:
                continue
            
            answer_type = topic_info['answer_type']
            cur_topic_ans = survey_new_answers[topic_name][f"{answer_type}_range"]

            updated_survey_topics[topic_name]['answer_type'] = answer_type
            # update topics
            topic_new_range = update_method_recall(
                cur_rounds_num=cur_rounds_num,
                topic_name=topic_name,
                topic_info=topic_info,
                survey_prev_answers=survey_prev_answers,
                cur_topic_ans=cur_topic_ans
            )
            if topic_new_range == TopicNoNeedUpdate:
                continue

            # TODO: 将updated_survey_topics变成选项
            # Turn updated_survey_topics that can be parsed by the front-end
            updated_survey_topics[topic_name]['choices_list'] = cls.__reformat_topic(
                topic_new_range=topic_new_range
            )

        return updated_survey_topics