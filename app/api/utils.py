from __future__ import annotations

from typing import Any

from typeguard import (
    check_type,
    typechecked
)

@typechecked
def check_if_data_is_valid(
    data: dict[str, Any],
    expected_data: list[dict[str, object]],
) -> None:
    '''
    1. Check if data is None
    2. Check if data type is correct

    Parameters
    ----------
    data : dict[str, Any]
    expected_data : list[dict[str, object]]

    Returns
    -------
    bool
    '''
    for expected_key, expected_type in expected_data.items():

        check_type(
            argname=f"{data[expected_key]}",
            value=data[expected_key],
            expected_type=expected_type,
        )

    return

