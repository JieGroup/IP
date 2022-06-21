from __future__ import annotations

from abc import ABC, abstractmethod

from app.dp.update_topics.update_method.static import StaticUpdate
from app.dp.update_topics.update_method.uniform import UniformUpdate

from typeguard import typechecked


class AbstractUpdateMethodFactory(ABC):

    @classmethod
    @abstractmethod
    def get_class(cls):
        pass


@typechecked
class GetStaticUpdate(AbstractUpdateMethodFactory):

    @classmethod
    def get_class(cls) -> type[StaticUpdate]:
        return StaticUpdate


@typechecked
class GetUniformUpdate(AbstractUpdateMethodFactory):

    @classmethod
    def get_class(cls) -> type[UniformUpdate]:
        return UniformUpdate


