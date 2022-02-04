import pytest
import pandas as pd

from calculator import Calculate

@pytest.mark.parametrize(
    "test_input, expected", 
    [("3+5", {"elevator":[1]}), 
    ("2+4", {"elevator":[]}), 
    ("6*9", {"elevator":[]})
    ],
)
def test_eval(test_input, expected):
    test_df = pd.DataFrame({"listing_id": [1], "desc_addinfo": [test_input]})
    result = Calculate().find_in_listings(test_df)
    assert result == expected
