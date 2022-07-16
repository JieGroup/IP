from app.utils.constant import Constant

from typeguard import typechecked

from datetime import (
    datetime, 
    timedelta, 
    timezone
)


@typechecked
class Time:

    '''
    Handle time related issue.
    Since datetime object cannot be serialized, we will transfer timestamp

    Attributes
    ----------
    None

    Methods
    -------
    get_expiration_utc_time
    get_current_utc_time
    '''

    @classmethod
    def is_time_period_valid(
        cls, time_period: int
    ) -> bool:
        '''
        If the time_period in second is greater than 2 months, return False

        Parameters
        ----------
        time_period : int
            Number of seconds

        Returns
        -------
        bool
        '''
        if time_period > Constant.TIME_PERIOD_UPPER_LIMIT:
            return False
        if time_period < Constant.TIME_PERIOD_LOWER_LIMIT:
            return False
        return True
    
    @classmethod
    def change_day_to_sec(
        cls,
        day: int
    ) -> int:
        '''
        Change day to second

        Parameters
        ----------
        day : int
            Number of day

        Returns
        -------
        int
        '''
        return day * 24 * 3600

    @classmethod
    def get_expiration_utc_time(
        cls, time_period: int
    ) -> int:

        '''
        Calculate expiration time based on utc time.

        Parameters
        ----------
        time_period : int
            Number of seconds

        Returns
        -------
        int

        Notes
        -----
        Cant use datetime.utcnow() or datetime.utcfromtimestamp().
        These 2 methods contain bugs.
        '''

        expiration_time = int((datetime.now(tz=timezone.utc) + timedelta(seconds=time_period)).timestamp())
        return expiration_time

    @classmethod
    def get_current_utc_time(cls) -> int:
        '''
        Calculate current time based on utc time.

        Parameters
        ----------
        None

        Returns
        -------
        int

        Notes
        -----
        Cant use datetime.utcnow() or datetime.utcfromtimestamp().
        These 2 methods contain bugs.
        '''
        current_time = int(datetime.now(tz=timezone.utc).timestamp())
        return current_time

    @classmethod
    def change_time_period_to_sec(
        cls,
        time_period: str
    ) -> int:
        '''
        Change time_period in day to second.

        Parameters
        ----------
        time_period : str

        Returns
        -------
        int
        '''
        time_period = int(time_period)
        time_period = cls.change_day_to_sec(day=time_period)
        return time_period