from __future__ import annotations

import pytest

from app.dp.update_topics.update_method.choices import (
    ReformatCategoricalTopic,
    ReformatContinuousTopic
)

from app.utils.api import Constant


class TestReformatChoices():

    @pytest.mark.parametrize(
        "topic_new_range, expected", 
        [
            (
                ['5', '6', '7'],
                [['5', '6', '7'], 'exclusion', 'stop']
            ),
            (
                [1, 15, 20],
                [[1, 15, 20], 'exclusion', 'stop']
            ),
        ]
    )
    def test_categorical_topic_reformat(self, topic_new_range, expected):
        
        assert expected == ReformatCategoricalTopic.reformat(
            topic_new_range=topic_new_range,
        )

    @pytest.mark.parametrize(
        "topic_new_range, expected", 
        [
            (
                (1, 5, 10),
                [{'min': 1, 'max': 5}, {'min': 6, 'max': 10}, 'stop']
            ),
            (
                (1, 15, 20),
                [{'min': 1, 'max': 15}, {'min': 16, 'max': 20}, 'stop']
            ),
        ]
    )
    def test_continuous_topic_reformat(self, topic_new_range, expected):
        
        assert expected == ReformatContinuousTopic.reformat(
            topic_new_range=topic_new_range,
        )
    
    