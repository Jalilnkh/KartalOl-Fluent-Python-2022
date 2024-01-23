# Example 15-5. Using a BookDict, but not quite as intended.

from chapter_classes import BookDict
from typing import TYPE_CHECKING

AUTHOR_ELEMENT = '<AUTHOR>{}</AUTHOR>'

def demo() -> None:
    book = BookDict(
        isbn='20241212',
        title='Kartal Ol',
        authors=['Jalil Kartal', 'Jabi'],
        pagecount=456
    )
    authors = book['authors']
    if TYPE_CHECKING:
        reveal_type(authors)
    authors = 'Jabi'
    book['wieght'] = 4.3
    del book['title']

def to_xml(book: BookDict) -> str:
    elements: list[str] = []
    for key, value in book.items():
        if isinstance(value, list):
            elements.extend(
                AUTHOR_ELEMENT.format(n) for n in value)
        else:
            tag = key.upper()
            elements.append(f'<{tag}>{value}</{tag}>')
    
    xml = '\n\t'.join(elements)
    return f'<BOOK>\n\t{xml}\n</BOOK>'


if __name__ == '__main__':
    demo()

"""
output:
Hints$ mypy book.py

book.py:13: note: Revealed type is "builtins.list[builtins.str]"
book.py:14: error: Incompatible types in assignment (expression has type "str", variable has type "list[str]")  [assignment]
book.py:15: error: TypedDict "BookDict" has no key "wieght"  [typeddict-unknown-key]
book.py:16: error: Key "title" of TypedDict "BookDict" cannot be deleted  [misc]
Found 3 errors in 1 file (checked 1 source file)
"""