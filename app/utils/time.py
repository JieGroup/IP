from app.utils.constant import Constant

from datetime import datetime, timedelta, timezone

class Time:

    @classmethod
    def is_time_period_valid(
        cls, time_period: int
    ) -> bool:

        # if the difference of time is greater than 2 months, return error
        if time_period > Constant.TIME_PERIOD_LIMIT:
            return False
        return True
    
    def get_expiration_time(
        cls, time_period: int
    ) -> str:

        expiration_time = (datetime.now(tz=timezone.utc) + timedelta(seconds=time_period)).timestamp()
        return expiration_time