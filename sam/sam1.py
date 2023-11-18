class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Книга '{self.title}', автор - {self.author}, год издания - {self.year}"

# Создаем объект класса "Книга"
book1 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)

# Выводим информацию о книге
print(book1.get_info())

# Создаем второй объект класса "Книга"
book2 = Book("1984", "Джордж Оруэлл", 1949)

# Выводим информацию о второй книге
print(book2.get_info())