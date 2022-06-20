from __future__ import annotations

import random
import numpy as np

from typeguard import typechecked

@typechecked
class ReformatBase:
    pass

@typechecked
class ReformatCategoricalTopic(ReformatBase):
    '''
    Class to reformat categorical updated
    topic to choices

    Attributes
    ----------
    None

    Methods
    -------
    reformat
    '''

    @classmethod
    def reformat(
        cls,
        topic_new_range: list[str]
    ) -> list[list[str], str, str]:
        '''
        Form a list of length 3.
        List[0] is the topic_new_range.
        List[1] means none of the options
        in list[0].
        List[2] means the user doesnt
        want to answer this topic.

        Parameters
        ----------
        topic_new_range : list[str]

        Returns
        -------
        list
        '''
        choices_list = [_ for _ in range(3)]
        choices_list[0] = topic_new_range
        choices_list[1] = 'exclusion'
        choices_list[2] = 'stop'

        return choices_list


class ReformatContinuousTopic(ReformatBase):
    '''
    Class to reformat continuous updated
    topic to choices

    Attributes
    ----------
    None

    Methods
    -------
    reformat
    '''

    @classmethod
    def reformat(
        cls,
        topic_new_range: tuple[int, int, int]
    ) -> list[dict[str, int], dict[str, int], str]:
        '''
        Form a list of length 3.
        List[0] contains min_val <= x <= new_mid_val
        List[1] contains new_mid_val+1 <= x <= max_val.
        List[2] means the user doesnt
        want to answer this topic.

        Parameters
        ----------
        topic_new_range : tuple[int, int, int]

        Returns
        -------
        list
        '''
        min_val = topic_new_range[0]
        new_mid_val = topic_new_range[1]
        max_val = topic_new_range[2]

        choices_list = [_ for _ in range(3)]
        choices_list[0] = {
            'min': min_val,
            'max': new_mid_val,
        }
        choices_list[1] = {
            'min': new_mid_val+1,
            'max': max_val
        }
        choices_list[2] = 'stop'
        
        return choices_list