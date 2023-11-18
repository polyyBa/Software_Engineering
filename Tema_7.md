# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил(а):
- Баталова Полина Андреевна
- ПИЭ-21-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |   |
| Задание 7 | + |   |
| Задание 8 | + |   |
| Задание 9 | + |   |
| Задание 10 | + |   |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.

### Результат
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/f9b01dde-0d7f-4354-be1d-b0405597a128)

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python 
f = open('input.txt', 'r')
print(f.readline())
f.close()
```

### Результат
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/240aa6d1-becb-4076-80c5-59976bd9af55)

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readlines())
f.close()
```

### Результат
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/c2364eaa-c923-4848-a846-52565e372c78)

## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    print(f.readlines())
```

### Результат
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/cc1a8477-8b08-4701-8454-e222d83e69af)

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    for line in f:
        print(line)
```

### Результат
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/830b0ef2-a870-4166-bd63-3243267729f4)

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
with open('input.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
```

### Результат
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/a806ad59-9f0e-48d1-9893-3cce9c289f10)

![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/15c99d83-71d7-4f92-bc9b-024ab0b4a58e)

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.

```python
lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```

### Результат
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/9d7ba71a-8ca5-4c1a-8914-a3310f6216ea)

### До
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/cc4a9382-739f-40a6-b663-28e123758388)
### После
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/3c66e889-819f-428d-bca9-5c72e84be0f5)

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).

```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)

print_docs('C:\\Users\Полина\Desktop\дизайн')
```

### Результат
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/15bbf7f3-1bcf-434f-b64e-aecddf838c2a)

## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст: Приветствие, Спасибо, Извините, Пожалуйста, До свидания, Ты готов?, Как дела?, С днем рождения!, Удача!, Я тебя люблю. Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных

```python
def longest_words(file):
    with open(file, encoding='utf-8' ) as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_words('input.txt'))
```

### Результат
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/fb4adbc2-4db4-4665-8daf-18e680c7960d)

## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
### № - номер по порядку (от 1 до 300);
### Секунда – текущая секунда на вашем ПК;
### Микросекунда – текущая миллисекунда на часах.
### Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for line in range(1,301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)
```

### Результат
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/ceab4bb2-aefe-4489-977d-b340eb1f18ef)

## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

```python
with open('статья.txt', encoding='utf-8') as f:
        words = f.read().split()
        word_count = len(words)
        print(f"В статье {word_count} слов.")
        word_freq = {}
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
most_word = max(word_freq, key=word_freq.get)
print(f"Самое часто встречающееся слово: '{most_word}' ({word_freq[most_word]} раз)")
```

### Результат (скриншот файла со статьей)
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/88102a5c-0d2a-4028-af53-087cb2a60397)

### Результат (вывод в консоль)
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/459f79f3-413a-44bc-9a1c-dc3257545175)

### Выводы
- Код открывает файл "статья.txt" с помощью функции open и читает его содержимое с помощью метода `read()`. Затем текст разбивается на слова с помощью метода `split()`, и количество слов сохраняется в переменной `word_count`.

- Далее создается пустой словарь `word_freq`, который будет использоваться для подсчета частоты встречаемости каждого слова. В цикле for происходит итерация по каждому слову в списке words. Если слово уже присутствует в словаре `word_freq`, то его значение увеличивается на 1. Если слово отсутствует в словаре, то оно добавляется в словарь со значением 1.

- После завершения цикла, находится самое часто встречающееся слово с помощью функции `max` и метода `get` словаря `word_freq`. Затем выводится информация о самом часто встречающемся слове и количестве его повторений.

## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
import json
def add_expense():
    date = input("Введите месяц расхода: ")
    item = input("Введите название расхода: ")
    cost = float(input("Введите сумму расхода: "))

    expense = {
        "date": date,
        "item": item,
        "cost": cost
    }

    with open('expenses.json', 'a') as file:
        json.dump(expense, file)
        file.write('\n')
    print("Расход успешно добавлен.")

def show_expenses():
    with open('expenses.json', 'r') as file:
        for line in file:
            expense = json.loads(line)
            print(f"Месяц: {expense['date']}, Название: {expense['item']}, Сумма: {expense['cost']}")

while True:
    choice = input("Выберите действие: 1 - добавить расход, 2 - показать все расходы, 3 - выход: ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        show_expenses()
    elif choice == '3':
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
```

### Результат (файла расходов)
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/c58adfb7-0fc1-4778-a2d1-eefe985ce0c4)

### Результат (вывод в консоль)
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/1e012839-8a25-4d73-b8c2-b3c334ba0608)

### Выводы
- Функция `add_expense` запрашивает у пользователя дату, название и сумму расхода. Затем создается словарь `expense`, содержащий эти данные. Далее происходит открытие файла "expenses.json" в режиме добавления `('a')`, и с помощью функции `json.dump` словарь expense записывается в файл в формате JSON. После этого в файл добавляется символ новой строки `('\n')`. В конце выводится сообщение о успешном добавлении расхода.

- Функция `show_expenses` открывает файл "expenses.json" в режиме чтения `('r')`. Затем происходит итерация по каждой строке файла. Для каждой строки вызывается функция `json.loads`, которая преобразует строку JSON в словарь. Затем выводится информация о расходе, включающая месяц, название и сумму.

- Главный цикл программы запрашивает у пользователя выбор действия: добавить расход, показать все расходы или выйти из программы. В зависимости от выбора вызывается соответствующая функция или происходит выход из цикла.

## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
### Текст в файле: Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated.
### Ожидаемый результат: Input file contains: 108 letters, 20 words, 4 lines/

```python
with open('input.txt', 'r') as file:
    text = file.read()
letters = sum(c.isalpha() for c in text)
words = len(text.split())
lines = text.count('\n') + 1

print(f"Input file contains: {letters} letters, {words} words, {lines} lines")
```

### Результат
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/8a567dad-b435-4a6b-8c85-d8faebc199c9)

### Выводы
- Код открывает файл с именем "input.txt" в режиме чтения и сохраняет его содержимое в переменную `text`. Затем он вычисляет количество букв в тексте путем подсчета количества символов, являющихся буквами для этого используется генератор списка с условием `c.isalpha()`.

- Далее код вычисляет количество слов в тексте, разделяя его на отдельные слова с помощью метода `split()` и считая количество полученных элементов. В конце, код вычисляет количество строк в тексте путем подсчета символов новой строки `\n` и добавления 1 (так как последняя строка может не содержать символа новой строки).

-Выводит результаты, а именно количество букв, слов и строк в файле, используя строковые форматирование для вставки значений в строку вывода.
   
## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
### Запрещенные слова: hello email python the exam wor is
### Предложение для проверки: Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!
### Ожидаемый результат: *****, ***ld! ****** ** *** programming language of *** future. My ***** **.... ****** ** awesome!!!!

```python
with open('inpput.txt') as forbidden_words, open('text.txt') as to_change:
	pattern, text = forbidden_words.read().split(), to_change.read()
text_lower = text.lower()
for word in pattern:
	text_lower = text_lower.replace(word, '*' * len(word))
result = ''.join((y, x)[x == '*'] for x, y in zip(text_lower, text))
print(result)
```

### Результат
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/562879bb-6d4d-41a1-8391-8fed419a87ad)

### Выводы
- Код открывает два файла: 'input.txt' для запрещённых слов и 'text.txt' для текста, который нужно изменить.
- Здесь используется контекстный менеджер `with`, который гарантирует, что файлы будут закрыты правильно даже в случае возникновения ошибки.
- В список `pattern` записываются запрещённые слова из файла 'input.txt'.
- В переменную `text` записывается содержимое файла 'text.txt'.
- Текст приводится к нижнему регистру для удобства сравнения.
- Каждое запрещённое слово заменяется символами '*' такой же длины в нижнем регистре.
- Создаётся строка `result`, в которой символы из `text` и `text_lower` соответственно выбираются в зависимости от того, является ли символ '*'.
- Результат выводится на экран с помощью `print`.


## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

Напишем программу на Python, которая будет читать файл "expenses.txt" и суммировать все расходы, предполагая, что каждая строка в файле представляет число (расход в долларах) после даты. После этого программа выведет общие расходы за месяц.

```python
with open('expenses.txt', 'r') as file:
    all_expenses = file.readlines()

total_expenses = 0

for line in all_expenses:
    expense = float(line)
    total_expenses += expense

print(f"Общие расходы за месяц составили ${total_expenses:.2f}")

new_expense = 42
with open('expenses.txt', 'a') as file:
    file.write(f"\n{new_expense}")
```

### Результат
![image](https://github.com/polyyBa/Software_Engineering/assets/144797777/146e0abf-f571-4eac-8ebc-f67504d6a3e4)

### Выводы

- Начинаем с открытия файла "expenses.txt" и чтения всех его строк.
- Затем инициализируем переменную `total_expenses` для хранения суммы всех расходов.
- Мы проходимся по каждой строке, предполагая, что она представляет число (расход в долларах), и суммируем все расходы.
- После этого выводим общую сумму расходов за месяц.
- Далее есть опциональный кусок кода, который позволяет добавить новый расход в файл "expenses.txt"
