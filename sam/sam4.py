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

book1 = Book("War and Peace", "Leo Tolstoy", 1869)
book2 = Book("Crime and Punishment", "Fyodor Dostoevsky", 1866)


class Ebook(Book):
    def __init__(self, title, author, year, format):
        super().__init__(title, author, year)
        self.format = format

    def get_info(self):
        return f"Title: {self._title}, Author: {self._author}, Year: {self._year}, Format: {self.format}"

ebook = Ebook("The Great Gatsby", "F. Scott Fitzgerald", 1925, "PDF")

print(ebook.get_info())
print(ebook.is_new_release())
ebook.change_author("Francis Scott Fitzgerald")
print(ebook.get_info())