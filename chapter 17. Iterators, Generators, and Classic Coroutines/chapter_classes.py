import re
import reprlib
from abc import ABC, abstractmethod, abstractproperty
from collections.abc import Iterable

RE_WORD = re.compile(r'\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    
    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        return SentenceIterator(self.words)
    
    

class SentenceIterator:

    def __init__(self, words) -> None:
        self.words = words
        self.index = 0
    
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index +=1
        return word
    
    def __iter__(self):
        return self
    
    
class Spam:
    def __getittem__(self, i):
        print('->', i)
        raise IndexError
    
    def __iter__(self):
        pass


class Iterator(Iterable):
    __slots__ = ()
    @abstractmethod
    def __next__(self):
        'Return the next item from the iterator. When exhausted, raise StopIteration'
        raise StopIteration
    def __iter__(self):
        return self
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterator:
            return _check_methods(C, '__iter__', '__next__')
        return NotImplemented
    

class Shape(ABC):
    def __init__(self, shape_name):
        self.shape_name = shape_name
    
    @abstractproperty
    def name(self):
        pass
     
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self):
        super().__init__("circle")
 
    @property
    def name(self):
        return self.shape_name
    
    def draw(self):    
        print("Drawing a Circle")


class Triangle(Shape):

    def __init__(self):
        super().__init__("triangle")

    def draw(self):
        print("Drawing a Triangle")