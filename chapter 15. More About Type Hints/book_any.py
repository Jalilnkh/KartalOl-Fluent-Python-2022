from chapter_classes import BookDict
import json


def from_json(data: str) -> BookDict:
    whatever = json.loads(data)
    return whatever

def from_json2(data: str) -> BookDict:
    whatever: BookDict = json.loads(data)
    return whatever
"""
Output:

Hints$ mypy book_any.py --disallow-any-expr
book_any.py:6: error: Expression has type "Any"  [misc]
book_any.py:7: error: Expression has type "Any"  [misc]
Found 2 errors in 1 file (checked 1 source file)

"""