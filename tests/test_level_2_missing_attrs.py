from typing import Union
from dataclasses import dataclass
from unittest.mock import Mock

@dataclass
class Book:
    title: str

class Author:
    def get_full_title() -> str:
        pass

class Review:
    @property
    def summary() -> str:
        pass

# Code to test:
def extract_title(item: Union[Book, Author, Review]) -> str:
    if isinstance(item, Book):
        return item.title
    
    if hasattr(item, "get_full_title"):
        return item.get_full_title()
    
    if hasattr(item, "summary"):
        return item.summary


# Tests:
def test_extract_title():
    book = Mock(spec=Book(""), title="Russian Literature")
    assert extract_title(book) == "Russian Literature"

    author = Mock(spec=Author)
    author.get_full_title.return_value = 'Alexandr Pushkin'
    assert extract_title(author) == 'Alexandr Pushkin'

    review = Mock(spec=Review)
    review.summary = 'Oh, bitter destiny'
    assert extract_title(review) == 'Oh, bitter destiny'
