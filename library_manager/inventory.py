import json
import logging
from pathlib import Path
from library_manager.book import Book

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DATA_FILE = Path("data/books.json")


class LibraryInventory:
    def __init__(self):
        self.books = []
        self.load_data()

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save_data()
        logging.info("Book added: %s", title)

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        if not self.books:
            print("No books in library.")
        for book in self.books:
            print(book)

    def save_data(self):
        try:
            DATA_FILE.parent.mkdir(exist_ok=True)
            with open(DATA_FILE, "w") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=4)
        except Exception as e:
            logging.error("Save error: %s", e)

    def load_data(self):
        try:
            if DATA_FILE.exists():
                with open(DATA_FILE, "r") as f:
                    data = json.load(f)
                    self.books = [Book(**item) for item in data]
        except Exception as e:
            logging.error("Load error: %s", e)
            self.books = []
