def add_two_numbers():
    try:
        num = int(input("Введите число: "))
        result = 2 + num
        print("Результат сложения:", result)
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

# Тест 1: ввод числа
add_two_numbers()

# Тест 2: ввод строки
add_two_numbers()

# Тест 3: ввод другого неподходящего типа данных
add_two_numbers()