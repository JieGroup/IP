from __future__ import annotations

import pytest

from app.api.utils import (
    check_if_data_is_valid
)

from typing import Union, List


class TestApiUtils():

    # @pytest.mark.parametrize(
    #     "data, expected_data", 
    #     [
    #         (
    #             {
    #                 'time_period': 5,
    #                 'number_of_copies': 6,
    #                 'max_rounds': 7,
    #                 'test_1': None,
    #                 'test_2': 5,
    #                 'test_3': ['4', '5']
    #             },
    #             {
    #                 'time_period': int,
    #                 'number_of_copies': int,
    #                 'max_rounds': int,
    #                 'test_1': Union[None, int],
    #                 'test_2': Union[None, int],
    #                 'test_3': list[str]
    #             }
    #         )
    #     ]
    # )
    # def test_check_if_data_is_valid(self, data, expected_data):
    #     check_if_data_is_valid(
    #         data=data,
    #         expected_data=expected_data
    #     )
    
    @pytest.mark.parametrize(
        "data, expected_data, wrong_key, wrong_key_type, expected_type", 
        [
            (
                {
                    'time_period': 5.5,
                    'number_of_copies': 6,
                    'max_rounds': 7
                },
                {
                    'time_period': int,
                    'number_of_copies': int,
                    'max_rounds': int,
                },
                'time_period',
                'float',
                'int',
            ),
        ]
    )
    def test_check_if_data_is_valid_exception_1(self, data, expected_data, wrong_key, wrong_key_type, expected_type):
        msg = f'type of {wrong_key} must be {expected_type}; got {wrong_key_type} instead'
        with pytest.raises(TypeError, match=msg):
            check_if_data_is_valid(
                data=data,
                expected_data=expected_data
            )
    
    # @pytest.mark.parametrize(
    #     "data, expected_data, wrong_key, wrong_key_type, expected_type", 
    #     [
    #         (
    #             {
    #                 'test_1': [5],
    #             },
    #             {
    #                 'test_1': List[str],
    #             },
    #             'test_1[0]',
    #             'int',
    #             'str',
    #         )
    #     ]
    # )
    # def test_check_if_data_is_valid_exception_2(self, data, expected_data, wrong_key, wrong_key_type, expected_type):
    #     msg = f'type of {wrong_key} must be {expected_type}; got {wrong_key_type} instead'
    #     with pytest.raises(TypeError, match=msg):
    #         check_if_data_is_valid(
    #             data=data,
    #             expected_data=expected_data
    #         )