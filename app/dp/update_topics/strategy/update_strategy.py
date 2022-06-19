from __future__ import annotations

from app.dp.update_topics.strategy.abstract_update_strategy import AbstractUpdateTopicsStrategy

from app.dp.update_topics.strategy.base import BaseUpdateTopicsStrategy

from app.dp.update_topics.update_method.api import (
    GetStaticUpdate,
    GetUniformUpdate
)

from typing import Union

from typeguard import typechecked

from app._typing import (
    Survey_Update_Method
)

@typechecked
class UpdateTopicsOperator(AbstractUpdateTopicsStrategy, BaseUpdateTopicsStrategy):

    def __init__(self) -> None:
        self.__update_method = None

    @property
    def update_method(self):
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self.__update_method

    @update_method.setter
    def update_method(self, update_method) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self.__update_method = update_method

    def set_update_method(
        self, update_method_type: Survey_Update_Method
    ) -> None:
        if update_method_type == 'static':
            self.__update_method = GetStaticUpdate.get_class()
        elif update_method_type == 'uniform':
            self.__update_method = GetUniformUpdate.get_class()

    def update_topics(
        self, **kwargs
    ) -> list:
        return self.__update_method.update_topics(**kwargs)