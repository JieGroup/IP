from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractUpdateTopicsStrategy(ABC):
    '''
    Abstract class for database strategy class.
    This is where our DatabaseOperator can override
    '''
    @abstractmethod
    def update_survey_topics(self, **kwargs):
        pass