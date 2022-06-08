from app.utils.constant import Constant

from datetime import datetime, timedelta

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
    ) -> type[datetime]:

        expiration_time = datetime.utcnow() + timedelta(seconds=time_period)
        return expiration_time