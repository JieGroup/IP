from __future__ import annotations

import pytest

from app.utils.api import (
    Time,
    Constant
)


class TestTime():

    @pytest.mark.parametrize(
        "time_period, expected", 
        [
            (Constant.TIME_PERIOD_UPPER_LIMIT+1, False),
            (Constant.TIME_PERIOD_LOWER_LIMIT-1, False),
            (Constant.TIME_PERIOD_UPPER_LIMIT, True),
            (Constant.TIME_PERIOD_LOWER_LIMIT, True)
        ]
    )
    def test_is_time_period_valid(self, time_period, expected):
        
        assert expected == Time.is_time_period_valid(
            time_period=time_period
        )
    
    @pytest.mark.parametrize("expected", [float])
    def test_get_expiration_utc_time_return_type(self, expected):
        
        assert expected == type(Time.get_expiration_utc_time(
            time_period=Constant.TIME_PERIOD_UPPER_LIMIT
        ))

    @pytest.mark.parametrize("expected", [float])
    def test_get_current_utc_time_return_type(self, expected):
        
        assert expected == type(Time.get_current_utc_time())
    
    def test_get_expiration_utc_time(self):
        
        expiration_time = Time.get_expiration_utc_time(
            time_period=Constant.TIME_PERIOD_LOWER_LIMIT
        )
        current_time = Time.get_current_utc_time()
        assert current_time < expiration_time