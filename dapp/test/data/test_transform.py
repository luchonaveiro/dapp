import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from dapp.data.transform import transform


def test_transform():
    raw_df = pd.DataFrame({"name": ["john"], "sex": ["m"], "salary": [10.5]})
    expected_df = pd.DataFrame(
        {"name": ["john"], "sex": ["M"], "salary": [10]}
    )
    actual_df = transform(raw_df)

    assert_frame_equal(actual_df, expected_df)
    assert actual_df["salary"][0] == 10


@pytest.fixture
def raw_df():
    raw_df = pd.DataFrame({"name": ["john"], "sex": ["m"], "salary": [10.5]})
    return raw_df


@pytest.mark.parametrize(
    "raw_value, expected_value", [(3.4, 3), (2.8, 2), (10.5, 10)]
)
def test_transform_parametrized(raw_value, expected_value):
    raw_df = pd.DataFrame(
        {"name": ["john"], "sex": ["m"], "salary": [raw_value]}
    )
    expected_df = pd.DataFrame(
        {"name": ["john"], "sex": ["M"], "salary": [expected_value]}
    )
    actual_df = transform(raw_df)

    assert_frame_equal(actual_df, expected_df)
