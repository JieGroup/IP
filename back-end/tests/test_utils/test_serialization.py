import copy
import pytest
import numpy as np
import pandas as pd

from app.error import DataTypeError

from app.utils.api import Serialization


class TestSerialization:

    @pytest.mark.parametrize("data, expected", [
        (np.array(5), 5),
        (np.array([5]), [5]),
        ({6}, [6]),
        (None, None),
        ({'5': np.array([[1, 2, 3], [4, 5, 6]])}, {'5': [[1, 2, 3], [4, 5, 6]]}),
        ([{'5': np.array([[1, 2, 3], [4, 5, 6]])}, '6'], [{'5': [[1, 2, 3], [4, 5, 6]]}, '6'])
    ])
    def test_make_data_serializable(self, data, expected):
        assert expected == Serialization.make_data_serializable(
            data=data
        )

    @pytest.mark.parametrize("data", [
        (pd.array(['a', 'b'], dtype=str), 5),
    ])
    def test_make_data_serializable_exception(self, data):
        
        msg = 'Data type wrong: not serializable'
        with pytest.raises(DataTypeError, match=msg):
            Serialization.make_data_serializable(
                data=data
            )


