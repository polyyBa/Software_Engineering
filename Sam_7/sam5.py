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