from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractUpdateTopicsStrategy(ABC):

    @classmethod
    @abstractmethod
    def get_class(cls):
        pass

    @abstractmethod
    def update_topics(self, **kwargs):
        pass