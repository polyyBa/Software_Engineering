# Создаем собственное исключение
class ValueTooSmallError(Exception):
    def __init__(self, message="Значение слишком мало"):
        self.message = message
        super().__init__(self.message)

# Используем исключение в первом фрагменте кода
def divide_numbers(x, y):
    if y <= 0:
        raise ValueTooSmallError("Знаменатель должен быть больше нуля")
    return x / y

try:
    result = divide_numbers(10, 10)  # Вызываем функцию divide_numbers с аргументами 10 и 0
except ValueTooSmallError as e:  # Ловим исключение ValueTooSmallError
    print(e)  # Выводим сообщение об ошибке

# Используем исключение во втором фрагменте кода
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueTooSmallError("Значения длины и ширины должны быть больше нуля")
    return length * width

try:
    area = calculate_area(5, 10)  # Вызываем функцию calculate_area с аргументами -5 и 10
except ValueTooSmallError as e:  # Ловим исключение ValueTooSmallError
    print(e)  # Выводим сообщение об ошибке