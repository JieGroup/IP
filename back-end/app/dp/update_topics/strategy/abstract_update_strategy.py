from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractUpdateTopicsStrategy(ABC):
    '''
    Abstract class for database strategy class.
    This is where our DatabaseOperator can override
    '''
    @classmethod
    @abstractmethod
    def get_class(cls):
        pass

    @abstractmethod
    def update_topics(self, **kwargs):
        pass