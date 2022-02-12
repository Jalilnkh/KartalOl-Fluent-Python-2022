"""
Let’s test-drive top. Example 8-22 shows part of a test suite for use with
pytest. It tries calling top first with a generator expression that yields
tuple[int, str], and then with a list of object. With the list of
object, we expect to get a TypeError exception.
"""
from collections.abc import Iterable
from typing import TYPE_CHECKING, TypeVar, Protocol, Any
from typing_extensions import reveal_type

import pytest

class SupportLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...

LT = TypeVar('LT', bound=SupportLessThan)

def top(series: Iterable[LT], length: int) -> list[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]

def test_top_tuples() -> None:
    fruit = 'mango pear apple kiwi banana'.split()
    series: Iterable[tuple[int, str]] = ((len(s), s) for s in fruit)
    length = 3
    excepted = [(6, 'banana'), (5, 'mango'), (5, 'apple')]
    result = top(series, length)
    if TYPE_CHECKING:
        reveal_type(series)
        reveal_type(excepted)
        reveal_type(result)
    assert result == excepted

def test_top_objects_error() -> None:
    series = [object() for _ in range(4)]
    if TYPE_CHECKING:
        reveal_type(series)
    with pytest.raises(TypeError) as excinfo:
        top(series, 3)
    assert "'<' not supported" in str(excinfo.value)
    