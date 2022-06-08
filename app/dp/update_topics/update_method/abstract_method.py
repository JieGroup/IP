from __future__ import annotations

from abc import ABC, abstractmethod

class AbstractUpdateMethod(ABC):

    @classmethod
    @abstractmethod
    def update_topics(cls, **kwargs):
        pass

    