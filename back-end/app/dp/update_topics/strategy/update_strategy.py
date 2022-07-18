from __future__ import annotations

from app.dp.update_topics.strategy.abstract_update_strategy import AbstractUpdateTopicsStrategy

from app.dp.update_topics.strategy.base import BaseUpdateTopicsStrategy

from app.dp.update_topics.update_method.api import (
    GetStaticUpdate,
    GetUniformUpdate
)

from typeguard import typechecked

from app._typing import (
    Survey_Update_Method
)

from typing import (
    final,
    Any,
    Callable,
    Union
)


@typechecked
class UpdateTopicsOperator(AbstractUpdateTopicsStrategy, BaseUpdateTopicsStrategy):
    '''
    Strategy pattern to update topics

    Attributes
    ----------
    update_method

    Methods
    -------
    set_update_method
    update_topics
    '''
    def __init__(self) -> None:
        self.__update_method = None

    @property
    def update_method(self) -> object:
        '''
        get strategy object
    
        Parameters
        ----------
        None

        Returns
        -------
        object
        '''
        return self.__update_method

    @update_method.setter
    def update_method(
        self, update_method: object
    ) -> None:
        '''
        set update_method to a strategy object

        Parameters
        ----------
        database : object

        Returns
        -------
        dict
        '''
        self.__update_method = update_method
        return

    def set_update_method(
        self, update_method_type: Survey_Update_Method
    ) -> None:
        '''
        function to help set strategy object

        Parameters
        ----------
        update_method_type : Survey_Update_Method

        Returns
        -------
        None
        '''
        if update_method_type == 'static':
            self.__update_method = GetStaticUpdate.get_class()
        elif update_method_type == 'uniform':
            self.__update_method = GetUniformUpdate.get_class()

    def update_survey_topics(
        self, **kwargs
    ) -> Union[None, dict[str, dict[str, Any]]]:
        '''
        strategy interface
        '''
        return self.__update_method.update_survey_topics(**kwargs)