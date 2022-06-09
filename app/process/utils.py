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

    return len(survey_prev_answers) + 1

