from __future__ import annotations

import collections
from multiprocessing.sharedctypes import Value

from typeguard import typechecked

from app.dp.update_topics.reformat.api import (
    StaticTopicReformat,
    UniformTopicReformat,
)

from app.error import TopicNoNeedUpdate

from app.utils.api import Constant

from app._typing import (
    Answer_Type,
    Survey_Update_Method,
    Survey_Topics,
    Survey_Prev_Answers,
    Survey_New_Answers,
    Categorical_Option_Type,
    Continuous_Option_Type
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
        max_rounds: int
    ) -> bool:
        '''
        Check if cur_rounds_num is valid

        Parameters
        ----------
        cur_rounds_num : int
            current round number
        max_rounds : int
            max round of all topics that can be 
            answered of this survey template

        Returns
        -------
        bool
        '''
        if 0 <= cur_rounds_num <= max_rounds:
            return True
        return False
    
    @final
    @classmethod
    def __if_survey_topics_need_updating(
        cls,
        cur_rounds_num: int,
        max_rounds: int
    ) -> bool:
        '''
        Check if survey_topics need updating

        Parameters
        ----------
        cur_rounds_num : int
            current round number
        max_rounds : int
            max round of all topics that can be 
            answered of this survey template

        Returns
        -------
        bool
        '''
        if 0 <= cur_rounds_num < max_rounds:
            return True
        return False
    
    # @final
    # @classmethod
    # def __is_cur_rounds_num_equals_one(
    #     cls, cur_rounds_num: int
    # ) -> bool:
    #     '''
    #     Check if cur_rounds_num is one

    #     Parameters
    #     ----------
    #     cur_rounds_num : int
    #         current round number

    #     Returns
    #     -------
    #     bool
    #     '''
    #     return cur_rounds_num == 1
    
    @final
    @classmethod
    def __reformat_topic(
        cls,
        survey_update_method: Survey_Update_Method,
        answer_type: Answer_Type,
        topic_new_range: Union[list, tuple] # first type for categorical, second for continuous
    ) -> Any:
        '''
        Turn the updated topics to choices that
        can be parsed by the front-end.

        Parameters
        ----------
        survey_update_method : Survey_Update_Method
        answer_type : Answer_Type
        topic_new_range :  Union[list[Categorical_Option_Type], tuple[Continuous_Option_Type]]
            updated topic     

        Returns
        -------
        Any
        '''
        print('??')
        if survey_update_method == 'static':
            return StaticTopicReformat.reformat_topic(
                answer_type=answer_type,
                topic_new_range=topic_new_range
            )
        elif survey_update_method == 'uniform':
            return UniformTopicReformat.reformat_topic(
                answer_type=answer_type,
                topic_new_range=topic_new_range
            )
        else:
            raise ValueError('survey_update_method wrong')

    @final
    @classmethod
    def update_topics_base_flow(
        cls,
        survey_update_method: Survey_Update_Method,
        cur_rounds_num: int, 
        max_rounds: int,
        survey_topics: Survey_Topics,
        survey_prev_answers: Survey_Prev_Answers,
        survey_new_answers: Survey_New_Answers,
        update_method_recall: Callable
    ) -> Union[None, dict[str, dict[str, Any]]]: # Topics new ranges
    # ) -> Any:
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
        print('xxxxxx----', cur_rounds_num)
        # Check if cur_rounds_num <= max_rounds_num
        if not cls.__is_cur_rounds_num_valid(
            cur_rounds_num=cur_rounds_num,
            max_rounds=max_rounds
        ):
            return {}
        print('zzzzzzz----')
        # Check if cur_rounds_num < max_rounds_num
        # If it is, we need to update the question
        if not cls.__if_survey_topics_need_updating(
            cur_rounds_num=cur_rounds_num,
            max_rounds=max_rounds
        ):
            return {}

        updated_survey_topics = collections.defaultdict(dict)
        for topic_name, topic_info in survey_topics.items(): 

            if topic_name not in survey_new_answers:
                continue
            
            answer_type = topic_info['answer_type']
            cur_topic_ans = survey_new_answers[topic_name][f"{answer_type}_range"]
            print('debug 5555')
            # update topics
            topic_new_range = update_method_recall(
                cur_rounds_num=cur_rounds_num,
                topic_name=topic_name,
                topic_info=topic_info,
                survey_prev_answers=survey_prev_answers,
                cur_topic_ans=cur_topic_ans
            )
            print('debug 666666')
            if topic_new_range == TopicNoNeedUpdate:
                continue
            print('####', topic_new_range, type(topic_new_range))
            # Turn updated_survey_topics that can be parsed by the front-end
            updated_survey_topics[topic_name]['answer_type'] = answer_type
            updated_survey_topics[topic_name]['choices_list'] = cls.__reformat_topic(
                survey_update_method=survey_update_method,
                answer_type=answer_type,
                topic_new_range=topic_new_range
            )
            updated_survey_topics[topic_name]['topic_question'] = topic_info['topic_question']
            updated_survey_topics[topic_name]['unit'] = topic_info['unit']
        print('###', updated_survey_topics)
        return updated_survey_topics
        