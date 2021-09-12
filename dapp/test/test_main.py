import pandas as pd
from pandas.testing import assert_frame_equal

from dapp.constants import RESOURCES_DIR
from dapp.data.load import load_csv
from dapp.data.transform import transform


def test_load(mocker):
    mocker.patch(
        "pandas.read_csv",
        return_value=pd.DataFrame(
            {"name": ["john"], "sex": ["m"], "salary": [10.5]}
        ),
    )
    expected_df = pd.DataFrame(
        {"name": ["john"], "sex": ["M"], "salary": [10]}
    )
    actual_df = transform(load_csv(RESOURCES_DIR / "data.csv"))

    assert_frame_equal(actual_df, expected_df)
