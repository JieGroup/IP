from __future__ import annotations

from abc import ABC, abstractmethod

from app.dp.update_topics.update_method.static import StaticUpdate
from app.dp.update_topics.update_method.uniform import UniformUpdate


class AbstractUpdateMethodFactory(ABC):

    @classmethod
    @abstractmethod
    def get_class(cls):
        pass


class GetStaticUpdate(AbstractUpdateMethodFactory):

    @classmethod
    def get_class(cls) -> type[StaticUpdate]:
        return StaticUpdate


class GetUniformUpdate(AbstractUpdateMethodFactory):

    @classmethod
    def get_class(cls) -> type[UniformUpdate]:
        return UniformUpdate


