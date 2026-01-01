from library_manager.book import Book

def test_book_issue():
    book = Book("Test", "Author", "123")
    assert book.issue() is True
    assert book.is_available() is False
