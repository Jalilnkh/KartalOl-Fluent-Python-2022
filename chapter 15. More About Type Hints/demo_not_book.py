# Example 15-11. demo_not_book.py: from_json returns an invalid
#BookDict, and to_xml accepts it.

from book import to_xml
from book_any import from_json2
from typing import TYPE_CHECKING

def demo() -> None:
    NOT_BOOK_JSON = """
    {"title": "Oshaglig",
    "flavor": "insan",
    "authors": true}
    """
    not_book = from_json2(NOT_BOOK_JSON)
    
    print(not_book)
    print(not_book['flavor'])

    xml = to_xml(not_book)
    print(xml)


if __name__ == '__main__':
    demo()
