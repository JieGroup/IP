from __future__ import annotations

from app.dp.update_topics.update_method.base import BaseUpdateMethod

from app.dp.update_topics.update_method.abstract_method import AbstractUpdateMethod

from typeguard import typechecked

from app._typing import Survey_Update_Method

from typing import (
    Union,
    Any
)


@typechecked
class StaticUpdate(AbstractUpdateMethod, BaseUpdateMethod):
    '''
    When the creator of the survey template chooses 
    StaticUpdate, the voter only needs to answer
    each topic in the survey once.

    Update topics is not needed for static mode.
    No funcion needs to be implemented.

    Attributes
    ----------
    None

    Methods
    -------
    generate_topic_new_range
    update_topics
    '''

    @classmethod
    def generate_topic_new_range(
        cls,
    ) -> None:
        pass
    
    @classmethod
    def update_topics(
        cls,
    ) -> None:

        pass

            