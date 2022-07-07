from __future__ import annotations

from typeguard import typechecked

from typing import final


@typechecked
class ValidateBase:
    '''
    Base class for Validation of new answers

    Attributes
    ----------
    None

    Methods
    -------
    None
    '''

    @final
    @classmethod
    def placeholder(cls):
        pass
