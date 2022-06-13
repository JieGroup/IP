from __future__ import annotations

import copy
import pytest

from app.utils.api import handle_response


class TestResponse:

    @pytest.mark.parametrize("key, container, expected", [
        (['key1', 'key2', 'key3'], {}, {'key1': {'key2': {}}}),
        (['key1'], {}, {})
    ])
    def test_process_key(self, key, container, expected):
        key_res, container_res = DictHelper.process_key(
            key=key,
            container=container
        )
        print('**', key, container)
        assert container == expected 

    