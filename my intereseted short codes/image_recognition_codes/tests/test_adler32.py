import pytest
from adler32 import Adler32


@pytest.mark.parametrize(
    "description,expected",
    [
        ("Algorithms", 363791387),
        ("go adler em all", 708642122),
    ],
)
def test_tbs(description, expected):

    results = Adler32().adler32(description)
    assert results == expected
