list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

set_1 = set()
for num in list_1:
    if list_1.count(num) > 1:
        set_1.add(str(num) * list_1.count(num))
    else:
        set_1.add(num)

set_2 = set()
for num in list_2:
    if list_2.count(num) > 1:
        set_2.add(str(num) * list_2.count(num))
    else:
        set_2.add(num)

set_3 = set()
for num in list_3:
    if list_3.count(num) > 1:
        set_3.add(str(num) * list_3.count(num))
    else:
        set_3.add(num)

print("Множество из list_1:", set_1)
print("Множество из list_2:", set_2)
print("Множество из list_3:", set_3)
