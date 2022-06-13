from __future__ import annotations

from typing import (
    final,
    Any,
    Callable,
    Union
)

def get_cur_rounds_num(
    survey_prev_answers: Union[None, dict[str, dict[str, Any]]]
) -> int:

    '''
    Get the number of rounds for the voter to answer the current survey

    Parameters
    ----------
    survey_prev_answers: Union[None, dict[str, dict[str, Any]]]. If
        we are at round 1, we dont have previous answers, thus the 
        current round number is 1.

    Returns
    -------
    int

    '''

    return len(survey_prev_answers) + 1

