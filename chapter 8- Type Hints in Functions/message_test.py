from pytest import mark
from messages import show_count


@mark.parametrize(
    'qty, expected',
    [
        (1, '1 part'),
        (2, '2 parts'),
    ],
)
def test_show_count(qty, expected) -> None:
    got = show_count(qty, 'part')
    assert got == expected


def test_count_zero() -> None:
    got = show_count(0, 'part')
    assert got == 'no parts'
