from __future__ import annotations

from werkzeug.security import generate_password_hash

def get_hashed_password(
    password: str
) -> str:

    '''
    Use werkzeug.security package to secure password

    Parameters
    ----------
    password : str
        password

    Returns
    -------
    str
        hashed password
    '''
    
    return generate_password_hash(password)