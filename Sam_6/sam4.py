def find_employee_movement(records, employee_id):
    if employee_id not in records:
        return ()

    start_index = records.index(employee_id)
    end_index = len(records) - 1 - records[::-1].index(employee_id)

    return records[start_index:end_index + 1]


records1 = (1, 2, 3)
records2 = (1, 8, 3, 4, 8, 8, 9, 2)
records3 = (1, 2, 8, 8, 5, 1, 2, 9)

print(find_employee_movement(records1, 8))
print(find_employee_movement(records2, 8))
print(find_employee_movement(records3, 8))