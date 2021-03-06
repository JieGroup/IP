from __future__ import annotations

from werkzeug.security import check_password_hash

from typing import Any

from typeguard import typechecked


@typechecked
def is_password_valid(
    hashed_password: str, 
    password: str
) -> bool:
    
    '''
    Check if hashed password matches the password that
    user re-type in.

    Parameters
    ----------
    hashed_password : str
        hashed password generated by werkzeug.security
    password : str
        password that user re-type in.
    
    Returns
    -------
    bool
    '''

    return check_password_hash(
        hashed_password,
        password
    )

@typechecked
def has_user_confirmed_email(
    cur_user_info: dict[str, Any]
) -> bool:

    '''
    check if current user has confirmed their email

    Parameters
    ----------
    cur_user_info : dict
        Information about current user. It is the user
        document previously stored in db.
    
    Returns
    -------
    bool
    '''

    if cur_user_info['confirm_email'] == False:
        return False
    return True