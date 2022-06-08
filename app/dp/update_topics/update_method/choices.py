from __future__ import annotations

import random
import numpy as np


class ReformatBase:
    pass


class ReformatCategoricalTopic(ReformatBase):

    @classmethod
    def reformat(
        cls,
        topic_new_range: list[str]
    ) -> list[dict[str, int], str, str]:

        '''
            We pick half elements in new_topic_range to form new
            categorical question
        '''

        if len(topic_new_range) > 1:
            sample_num = np.ceil(len(topic_new_range)/2.0).astype(int)
            # half-sample to obtain the subset to ask
            topic_new_range = random.sample(topic_new_range, sample_num)

        choices_list = [_ for _ in range(3)]
        choices_list[0] = topic_new_range
        choices_list[1] = 'exclusion'
        choices_list[2] = 'stop'

        return choices_list


class ReformatContinuousTopic(ReformatBase):

    @classmethod
    def reformat(
        cls,
        topic_new_range: tuple[int, int, int]
    ) -> list[dict[str, int], dict[str, int], str]:

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


# Reformat new topics in updated_survey_topics that can be
# used easily in front-end 