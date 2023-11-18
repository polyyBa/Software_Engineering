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