grades = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

new_grades = []

for grade in grades:
    if grade == 2:
        continue
    elif grade == 3:
        new_grades.append(4)
    else:
        new_grades.append(grade)

print("Обновленный список оценок:", new_grades)