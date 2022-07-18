from __future__ import annotations

import copy
import numpy as np

from app.dp.update_topics.reformat.base import BaseReformat

from typeguard import typechecked

from typing import (
    Union,
    Any
)

from app._typing import (
    Categorical_Option_Type,
    Continuous_Option_Type,
    Answer_Type
)


@typechecked
class StaticTopicReformat(BaseReformat):
    '''
    Class to reformat categorical updated
    topic to choices

    Attributes
    ----------
    None

    Methods
    -------
    reformat_topic
    '''
    @classmethod
    def reformat_topic(
        cls,
        answer_type: Answer_Type,
        topic_new_range: Union[list, tuple]
    ) -> Any:
        print('???')
        if answer_type == 'categorical':
            return cls.__reformat_categorical_topic(
                topic_new_range=topic_new_range
            )
        elif answer_type == 'continuous':
            return cls.__reformat_continuous_topic(
                topic_new_range=topic_new_range
            )

    @classmethod
    def __reformat_categorical_topic(
        cls,
        topic_new_range: list[Categorical_Option_Type]
    ) -> list[dict[str, Union[list, str]]]:
        '''
        Reformat categorical updated topic to choices
        Form a list of length 3.

        List[0] is the topic_new_range.
        List[1] means the user doesnt
        want to answer this topic.

        Parameters
        ----------
        topic_new_range : list[Categorical_Option_Type]

        Returns
        -------
        list[dict[str, Union[list, str]]]
        '''
        choices_list = [_ for _ in range(2)]
        choices_list[0] = {
            'inclusion': copy.deepcopy(topic_new_range)
        }
        choices_list[1] = {
            'stop': 'stop'
        }
        
        return choices_list

    @classmethod
    def __reformat_continuous_topic(
        cls,
        topic_new_range: tuple[Continuous_Option_Type, Continuous_Option_Type]
    ) -> list[Union[dict[str, Continuous_Option_Type], str]]:
        '''
        Reformat continuous updated topic to choices

        Form a list of length 3.
        List[0] contains min_val <= x <= new_mid_val
        List[1] means the user doesnt
        want to answer this topic.

        Parameters
        ----------
        topic_new_range : tuple[Continuous_Option_Type, Continuous_Option_Type, Continuous_Option_Type]

        Returns
        -------
        list
        '''
        print(f'topic_new_range: {topic_new_range}')
        min_val = topic_new_range[0]
        max_val = topic_new_range[1]

        choices_list = [_ for _ in range(2)]
        choices_list[0] = {
            'min': min_val,
            'max': max_val,
        }
        choices_list[1] = 'stop'
        
        return choices_list

    