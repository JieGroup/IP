from __future__ import annotations

import pytest

from tests.test_dp.test_update_method.conftest import StaticUpdate


class TestStaticUpdate():

    @pytest.mark.usefixtures('StaticUpdate')
    def test_static_update(self, StaticUpdate):
        '''
        The static update does not need implementation.
        We simply check if it can run.
        '''
        StaticUpdate.generate_topic_new_range()
        StaticUpdate.update_topics()

    