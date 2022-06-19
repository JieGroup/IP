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


    for expected_key, expected_type in expected_data.items():

        check_type(
            argname=f"{data[expected_key]}",
            value=data[expected_key],
            expected_type=expected_type,
        )

    return

