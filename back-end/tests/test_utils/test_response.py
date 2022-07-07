from __future__ import annotations

import copy
import pytest

from app.utils.api import handle_response

from typeguard import check_type
from app._typing import JSONType


class TestResponse():

    @pytest.mark.parametrize("expected", [
        JSONType
    ])
    def test_response(self, expected):
        
        @handle_response
        def test(data: int):
            return data
        
        print(type(test(5)))
        check_type(
            value=test(5),
            expected_type=expected,
            argname='check_response_type'
        )
        
        return
    