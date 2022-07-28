from __future__ import annotations

import json

from flask import g

from app.utils.serialization import Serialization

from typeguard import typechecked

from functools import wraps

from typing import Callable

from app._typing import JSONType


@typechecked
def handle_response(
    func: Callable
) -> Callable:
    
    @wraps(func)
    def wrapper(
        *args, **kwargs
    ) -> JSONType:
        '''
        1. Handle type of return data
        2. Add token
        '''
        print('daohandlele')
        res = func(*args, **kwargs)
        print('g handle_response', g)
        # print('g.current_user', g.current_user)
        if 'userToken' in g:
            res['userToken'] = g.userToken
        if 'voterToken' in g:
            res['voterToken'] = g.voterToken
        res = Serialization.make_data_serializable(res)
        return json.dumps(res)

    return wrapper