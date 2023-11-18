# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил(а):
- Баталова Полина Андреевна
- ПИЭ-21-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python
class Car: # объявляем класс «Car»
    def __init__(self, make, model): # определение конструктора класса "init". Конструктор принимает два аргумента «make» и «model»
        self.make = make # присваиваем значение аргумента «make» атрибуту «self.make»
        self.model = model # присваиваем значение аргумента «model» и атрибута «self.model»

my_car = Car("Toyota", "Corolla") #создаем экземпляр класса «Car» с аргументами «Toyota» и «Corolla» и применяем переменную «my_car»
```

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car: # объявляем класс «Car»
    def __init__(self, make, model): # определение конструктора класса "init". Конструктор принимает два аргумента «make» и «model»
        self.make = make # присваиваем значение аргумента «make» атрибуту «self.make»
        self.model = model # присваиваем значение аргумента «model» и атрибута «self.model»

    def drive(self): # определяем метод "drive"
        print(f"Driving the {self.make} {self.model}") # метод выводит сообщение о том, что происходит вождение автомобиля

my_car = Car("Toyota", "Corolla") # создаем экземпляр класса «Car» с аргументами «Toyota» и «Corolla» и применяем переменную «my_car»
my_car.drive() # вызываем метод "drive" для экземпляра класса "my_car"
```
### Результат.
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/06d6283f-390a-4b5b-8912-ccd84e15614e)

## Лабораторная работа №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться.Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль. 

```python
class ElectricCar(Car): # создаем новый класс ElectricCar, который является подклассом класса Car
    def __init__(self, make, model, battery_capacity): # определяем метод init для класса ElectricCar, который принимает аргументы марки, модели и емкости батареи
        super().__init__(make,model) # вызываем метод init родительского класса Car с помощью функции super(), переопределяющей аргументы make и model
        self.battery_capacity = battery_capacity # сохраняем значение аргумента Battery_Capacity в атрибуте self.battery_capacity

    def charge(self): # определяем метод зарядки для класса ElectricCar
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh") # вывод сообщения о марке зарядного устройства и модели автомобиля с указанием емкости аккумулятора

my_electric_car = ElectricCar("Tesla", "Model S", 75) # создаем экземпляр класса ElectricCar с аргументами «Тесла», «Модель S», 75 и сохраняем его в переменной my_electric_car
my_electric_car.drive() # вызываем метод Drive() у экземпляра my_electric_car, который реализован в родительском классе Car
my_electric_car.charge() # вызываем метод charge() у экземпляра my_electric_car, который находится в классе ElectricCar, и выводим информацию о зарядке
```
### Результат.
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/0c22e936-8dfe-49cb-98bd-9413654c0e19)

## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car: # объявляем класс «Car»
    def __init__(self, make, model): # определение конструктора класса "init". Конструктор принимает два аргумента «make» и «model»
        self._make = make # присваиваем значение аргумента «make» защищенному атрибуту «self._make»
        self.__model = model # присваиваем значение аргумента «model» и приватного атрибута «self.__model»

    def drive(self): # определяем метод "drive"
        print(f"Driving the {self._make} {self.__model}") # метод выводит сообщение о том, что происходит вождение автомобиля

my_car = Car("Toyota", "Corolla") # создаем экземпляр класса «Car» с аргументами «Toyota» и «Corolla» и применяем переменную «my_car»
print(my_car._make) # доступ к защищенному атрибуту
# print(my_car.__model) # Приватный атрибут не доступен
my_car.drive() # вызываем метод "drive" для экземпляра класса "my_car"
```
### Результат.
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/a2e7b492-36ac-4ece-ba42-6b95e9874659)

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
# Создаем основной класс Shape
class Shape:
    # Определяем метод для подсчета площади, который будет переопределен в дочерних классах
    def area(self):
        pass

# Создаем дочерний класс Rectangle, наследующийся от класса Spape
class Rectangle(Shape):
    # Инициализируем класс с заданными шириной и высотой
    def __init__(self, width, height):
        self.widht = width
        self.height = height

    # Переопределяем метод для подсчета площади прямоугольника
    def area(self):
        return self.widht * self.height

# Создаем дочерний класс Круг, наследующийся от класса Spape
class Circle(Shape):
    # Инициализируем класс с заданным радиусом
    def __init__(self, radius):
        self.radius = radius

    # Переопределяем метод для подсчета площади круга
    def area(self):
        return 3.14 * self.radius * self.radius

# Создаем массив с фигурами
figures = [Rectangle(4, 5), Circle(3)]

# Перебираем фигуры в массиве
for figure in figures:
    # Вызываем метод area() для каждой фигуры и выводим результат
    print("Площадь равна", figure.area())
```
### Результат.
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/54161fd4-bbc9-43e7-9fc9-7dd628862c34)

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Книга '{self.title}', автор - {self.author}, год издания - {self.year}"

book1 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)

print(book1.get_info())

book2 = Book("1984", "Джордж Оруэлл", 1949)

print(book2.get_info())
```
### Результат.
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/887cd42b-bd87-40f7-802b-9f0eae9c545f)

## Выводы

- Код создает класс "Книга", который имеет атрибуты "название", "автор" и "год издания". У класса есть метод `get_info`, который возвращает информацию о книге. Затем создаются два объекта класса "Книга" - `book1` и `book2`, и выводится информация о каждой книге.

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```
### Результат.
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/1deeec81-b4c8-41a4-ae92-d1c1a88d1fea)

## Выводы
- Код определяет класс `Book`, который представляет книгу. Класс имеет конструктор, который инициализирует атрибуты title, author и year. Класс также имеет методы `get_info` для получения информации о книге, `is_new_release` для проверки, является ли книга новым выпуском, и `change_author` для изменения автора книги.

- В коде создаются две книги: book1 и book2. Затем выводится информация о каждой книге с помощью метода `get_info`.

- Затем проверяется, являются ли книги новыми выпусками с помощью метода `is_new_release`. Если книга была выпущена в течение последнего года, метод возвращает `True`, в противном случае - `False`.

- Затем автор книги book1 изменяется на "Leo Tolstoy" с помощью метода `change_author`, и снова выводится информация о книге с помощью метода `get_info`.
  
## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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


class Ebook(Book):
    def __init__(self, title, author, year, format):
        super().__init__(title, author, year)
        self.format = format

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Format: {self.format}"

ebook = Ebook("The Great Gatsby", "F. Scott Fitzgerald", 1925, "PDF")

print(ebook.get_info())
print(ebook.is_new_release())
ebook.change_author("Francis Scott Fitzgerald")
print(ebook.get_info())
```
### Результат.
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/ff673ee4-4407-4dd1-8610-985306c35c25)

## Выводы

- Для реализации наследования создадим новый класс `Ebook`, который будет наследоваться от класса `Book`
  
- В конструкторе класса Ebook мы вызываем конструктор класса Book с помощью функции `super()`, чтобы инициализировать атрибуты title, author и year. Затем мы добавляем новый атрибут format.

- Метод `get_info` переопределяется в классе Ebook, чтобы возвращать информацию о книге с учетом формата.

- Далее создаем экземпляр класса Ebook и вызваем его методы с выводом в консоль.
  
## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```
### Результат.
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/d8d09d75-9aaf-4d05-9e7b-5e7b7c4ad1d7)

## Выводы

- Для реализации инкапсуляции в классе Book мы можем изменить модификаторы доступа атрибутов title, author и year на private (символ _ перед именем атрибута)
- Теперь атрибуты title, author и year стали защищенными и не могут быть напрямую доступны извне класса. Однако, мы всё еще можем получить к ним доступ через методы класса
  
## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```
### Результат.
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/4db2fbf2-f798-433d-88dc-a0e41db999f6)

## Выводы

- В коде мы переопределили метод get_info в классе Ebook, добавив информацию о формате книги. Теперь при вызове метода `get_info` для объекта класса Ebook, будет возвращаться строка с дополнительной информацией о формате
- Метод `get_info` работает с объектами классов Book и Ebook, возвращая разные результаты в зависимости от типа объекта.
