import pytest

from main import BooksCollector

@pytest.fixture(scope = 'function')
def book():
    book = 'Обломов'
    return book

@pytest.fixture(scope = 'function')
def genre():
    genre = 'Ужасы'
    return genre

@pytest.fixture(scope = 'function')
def collector():
    collector = BooksCollector()
    return collector