from __future__ import annotations

from abc import ABC, abstractmethod

class AbstractUpdateMethod(ABC):
    '''
    Abstract class for UpdateMethod class.
    This is where our UpdateMethod class can override
    '''
    @classmethod
    @abstractmethod
    def generate_topic_new_range(cls, **kwargs):
        pass
    
    @classmethod
    @abstractmethod
    def update_topics(cls, **kwargs):
        pass

    