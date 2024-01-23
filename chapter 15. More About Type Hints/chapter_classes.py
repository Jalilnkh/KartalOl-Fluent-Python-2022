import abc
import random
from collections.abc import Iterable
from typing import TypedDict, Generic, TypeVar


T = TypeVar('T')

class BookDict(TypedDict):
    isbn: str
    title: str
    authors: list[str]
    pagecount: int


class Rectangle:
    # ... lines omitted ...
    def stretch(self, factor: float) -> 'Rectangle':
        return Rectangle(width=self.width * factor)


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable."""
    @abc.abstractmethod
    def pick(self):
        """Remove item at random, returning it.
        This method should raise `LookupError` when the instance is
        empty.
        """
    def loaded(self):
        """Return `True` if there's at least 1 item, `False`
        otherwise."""
        return bool(self.inspect())
    def inspect(self):
        """Return a sorted tuple with the items currently
        inside."""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(items)
        


class LottoBlower(Tombola, Generic[T]):

    def __init__(self, items: Iterable[T]) -> None:
        self._balls = list[T](items)

    def load(self, items: Iterable[T]) -> None:
        self._balls.extend(items)

    def pick(self) -> T:
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LottoBlower')
        return self._balls.pop(position)

    def loaded(self) -> bool:
        return bool(self._balls)

    def inspect(self) -> tuple[T, ...]:
        return tuple(self._balls)
    
