from __future__ import annotations

from flask.json import jsonify

from app.utils.api import Serialization

from typing import (
    Any
)

from app._typing import JSONType

def handle_response(
    func: Any
) -> JSONType:

    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        res = Serialization.make_data_serializable(res)
        return jsonify(res)

    return wrapper