import sys
import re
import unicodedata
from collections.abc import Iterator
from numpy import mat
import collections

# how yield works
def print_even(test_list):
    for i in test_list:
        if i % 2 == 0:
            yield i


test_list = [1, 2, 3, 4, 6, 8]
for j in print_even(test_list):
    print(j, end=" ")


def nestSquare():
    i = 1
    while True:
        yield i * i
        i += 1


for num in nestSquare():
    if num > 100:
        break
    print(num)


RE_WORD = re.compile(r"\w+")
STOP_CODE = sys.maxunicode + 1


def tokenize(text: str) -> Iterator[str]:
    """return iterable of uppercased words"""
    for match in RE_WORD.finditer(text):
        yield match.group().upper()


def name_index(start: int = 32, end: int = STOP_CODE) -> dict[str, set[str]]:
    index = collections.defaultdict(list)
    for char in (chr(i) for i in range(start, end)):
        if name := unicodedata.name(char, ""):
            for word in tokenize(name):
                index[word].append(char)
    return index


index = name_index(32, 64)

print(index["SIGN"])
print(index["DIGIT"])
