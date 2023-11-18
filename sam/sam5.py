from datetime import datetime

class Book:
    def __init__(self, title, author, year):
        self._title = title
        self._author = author
        self._year = year

    def get_info(self):
        return f"Title: {self._title}, Author: {self._author}, Year: {self._year}"

    def is_new_release(self):
        current_year = datetime.now().year
        return current_year - self._year <= 1

    def change_author(self, new_author):
        self._author = new_author


class Ebook(Book):
    def __init__(self, title, author, year, format):
        super().__init__(title, author, year)
        self._format = format

    def get_info(self):
        return f"{super().get_info()}, Format: {self._format}"

book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
ebook = Ebook("The Catcher in the Rye", "J.D. Salinger", 1951, "EPUB")

print(book.get_info())
print(ebook.get_info())