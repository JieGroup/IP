from __future__ import annotations

from flask import g

from typing import Any

from typeguard import (
    check_type,
    typechecked
)

@typechecked
def check_if_data_is_valid(
    data: dict[str, Any],
    expected_data: dict[str, object],
) -> None:
    '''
    1. Check if data is None
    2. Check if data type is correct

    Parameters
    ----------
    data : dict[str, Any]
    expected_data : dict[str, object]

    Returns
    -------
    bool
    '''
    for expected_key, expected_type in expected_data.items():
        check_type(
            argname=f'{expected_key}',
            value=data[expected_key],
            expected_type=expected_type,
        )
    return

def get_user_id_from_token():
    '''
    Return the user_id parsed from token

    Parameters
    ----------
    None

    Returns
    -------
    str
    '''
    user_id = g.current_user['user_id']
    return user_id

def is_request_user_id_valid(
    cur_user_id: str, 
    request_user_id: str
) -> bool:
    '''
    Check if request_user_id is equal
    to current user id

    Parameters
    ----------
    cur_user_id : str
    request_user_id : str

    Returns
    -------
    bool
    '''
    return cur_user_id == request_user_id