from __future__ import annotations

import json

from app.utils.serialization import Serialization

from typeguard import typechecked

from functools import wraps

from typing import Callable

from app._typing import JSONType


@typechecked
def handle_response(
    func: Callable
) -> Callable:
    print('daohandlele')

    @wraps(func)
    def wrapper(
        *args, **kwargs
    ) -> JSONType:

        res = func(*args, **kwargs)
        res = Serialization.make_data_serializable(res)
        return json.dumps(res)

    return wrapper