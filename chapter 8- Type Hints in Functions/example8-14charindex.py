#%%
import sys
import re
import unicodedata
from collections.abc import Iterator
#%%
from numpy import mat

RE_WORD = re.compile(r'\w+')
STOP_CODE = sys.maxunicode + 1

def tokenize(text: str) -> Iterator[str]:
    """return iterable of uppercased words"""
    for match in RE_WORD.finditer(text):
        yield match.group().upper()

def name_index(start: int=32, 
                end: int=STOP_CODE) -> dict[str, set[str]]:
    index: dict[str, set[str]] = {}
    for char in (chr(i) for i in range(start, end)):
        if name := unicodedata.name(char, ''):
            for word in tokenize(name):
                index.setdefault(word, set()).add(char)
    return index

index = name_index(32, 64)

print(index['SIGN'])
print(index['DIGIT'])

