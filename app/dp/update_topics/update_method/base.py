from __future__ import annotations

import collections
from typing import (
    final,
    Any,
    Callable,
    Union
)



from app.dp.update_topics.update_method.choices import (
    ReformatCategoricalTopic,
    ReformatContinuousTopic,
)


class BaseUpdateMethod:
    """
    Base class for Algorithm
    """

    # TODO: implement methods
    @final
    def placeholder(self):
        pass

    @final
    @classmethod
    def if_cur_rounds_num_valid(
        cls,
        cur_rounds_num: int,
        max_rounds_of_survey: int
    ) -> bool:
        
        if cur_rounds_num <= max_rounds_of_survey:
            return True
        return False
    
    @final
    @classmethod
    def if_survey_topics_need_updating(
        cls,
        cur_rounds_num: int,
        max_rounds_of_survey: int
    ) -> bool:

        if cur_rounds_num < max_rounds_of_survey:
            return True
        return False
    
    @final
    @classmethod
    def if_cur_rounds_num_equals_one(
        cls, cur_rounds_num: int
    ) -> bool:

        return cur_rounds_num == 1

    
    @final
    @classmethod
    def reformat_topic(
        cls,
        answer_type: str,
        # first one for categorical, second for continuous
        topic_new_range: Union[list[str], tuple[int, int, int]] 
    ) -> list[dict, str]:

        if answer_type == 'categorical':
            return ReformatCategoricalTopic.reformat(
                topic_new_range=topic_new_range
            )
        elif answer_type == 'continuous':
            return ReformatContinuousTopic.reformat(
                topic_new_range=topic_new_range
            )
        else:
            # error
            return

   
    @final
    @classmethod
    def update_topics_base_flow(
        cls,
        cur_rounds_num: int, 
        max_rounds: int,
        survey_topics: dict[dict[str, Any]],
        survey_prev_answers: dict[str, Union[str, Any]],
        survey_new_answers: dict[dict[str, Any]],
        update_method_recall: Callable
    ) -> dict[str, dict[str, Any]]: # Topics new ranges

        '''
        Abstracting out common workflows that every update method 
        needs to go through 

        Parameters
        ----------
        cur_rounds_num : int
            
        time_period : int
            Defines how long we should keep the survey template in database
        max_rounds : int
            Defines how many times the topic can be regenerated
        number_of_copies : int
            Defines the max number of survey to issue
        survey_topics :
            The detailed information of each topic

        Returns
        -------
        bool
        '''

        # Check if cur_rounds_num <= max_rounds_num
        if not cls.if_cur_rounds_num_valid(
            cur_rounds_num=cur_rounds_num,
            max_rounds=max_rounds
        ):
            return None
                
        # Check if cur_rounds_num < max_rounds_num
        # If it is, we need to update the question
        if not cls.if_survey_topics_need_updating(
            cur_rounds_num=cur_rounds_num,
            max_rounds=max_rounds
        ):
            return None

        updated_survey_topics = collections.defaultdict(dict)
        for topic_name, topic_info in survey_topics.items(): 

            answer_type = topic_info['answer_type']
            cur_topic_ans = survey_new_answers[topic_name][f"{answer_type}_range"]

            updated_survey_topics[topic_name]['answer_type'] = answer_type
            topic_new_range = update_method_recall(
                cur_rounds_num=cur_rounds_num,
                topic_name=topic_name,
                topic_info=topic_info,
                survey_prev_answers=survey_prev_answers,
                cur_topic_ans=cur_topic_ans
            )

            # TODO: 将updated_survey_topics变成选项
            updated_survey_topics[topic_name]['choices_list'] = cls.reformat_topic(
                topic_new_range=topic_new_range
            )

        return updated_survey_topics