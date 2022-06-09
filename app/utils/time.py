from app.utils.constant import Constant

from datetime import datetime, timedelta, timezone

class Time:

    '''
    Handle time related issue.
    Since datetime object cannot be serialized, we will transfer timestamp

    Attributes
    ----------
    None

    Methods
    -------
    get_expiration_time
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

        if time_period > Constant.TIME_PERIOD_LIMIT:
            return False
        return True
    
    def get_expiration_time(
        cls, time_period: int
    ) -> str:

        '''
        Calculate expiration time based on utc time.

        Parameters
        ----------
        time_period : int
            Number of seconds

        Returns
        -------
        str

        Notes
        -----
        Cant use datetime.utcnow() or datetime.utcfromtimestamp().
        These 2 methods contain bugs.
        '''

        expiration_time = (datetime.now(tz=timezone.utc) + timedelta(seconds=time_period)).timestamp()
        return expiration_time