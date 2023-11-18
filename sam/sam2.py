from datetime import datetime

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

    def is_new_release(self):
        current_year = datetime.now().year
        return current_year - self.year <= 1

    def change_author(self, new_author):
        self.author = new_author

# Создание экземпляров класса Book
book1 = Book("War and Peace", "Leo Tolstoy", 1869)
book2 = Book("Crime and Punishment", "Fyodor Dostoevsky", 1866)

# Вывод информации о каждой книге
print(book1.get_info())
print(book2.get_info())

# Проверка, являются ли книги новыми выпусками
print(book1.is_new_release())
print(book2.is_new_release())

# Изменение автора книги book1
book1.change_author("Leo Tolstoy")

# Вывод информации о книге book1 после изменения автора
print(book1.get_info())