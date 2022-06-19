""" basic inference routines """

from collections import abc
from numbers import Number
import re
from typing import Pattern
import warnings

import numpy as np
import pandas as pd

from pandas.api.types import is_dict_like as pandas_is_dict_like
from pandas.api.types import is_integer as pandas_is_integer
from pandas.api.types import is_list_like as pandas_is_list_like
from pandas.api.types import is_float as pandas_is_float

from typeguard import typechecked

from typing import (
    Any,
    Literal
)


def is_numpy(obj) -> bool:
    return isinstance(obj, (np.ndarray, np.generic))

def is_dict_like(obj) -> bool:
    return pandas_is_dict_like(obj)

def is_list_like(obj) -> bool:
    return pandas_is_list_like(obj)

def is_tuple(obj) -> bool:
    return isinstance(obj, tuple)

def is_list(obj) -> bool:
    return isinstance(obj, list)

def is_integer(obj) -> bool:
    return pandas_is_integer(obj)

def is_float(obj) -> bool:
    return pandas_is_float(obj)

def is_set(obj) -> bool:
    return type(obj) == set

def is_datetime_dot_datetime(obj) -> bool:
    from datetime import datetime
    return type(obj) == datetime

# @typechecked
# def is_var_in_literal(
#     var: Any,
#     expected_type: Literal
# ) -> bool:
#     '''
#     Check if var is in expected_type

#     Parameters
#     ----------
#     var : Any

#     Returns
#     -------
#     bool
#     '''
#     return var in expected_type.__args__

