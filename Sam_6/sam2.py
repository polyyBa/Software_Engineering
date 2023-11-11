def remove_first_occurrence(tup, element):
    if element in tup:
        index = tup.index(element)
        new_tup = tup[:index] + tup[index+1:]
        return new_tup
    else:
        return tup


tup1 = (1, 2, 3)
tup2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
tup3 = (2, 4, 6, 6, 4, 2)

result1 = remove_first_occurrence(tup1, 1)
result2 = remove_first_occurrence(tup2, 3)
result3 = remove_first_occurrence(tup3, 9)

print(result1)
print(result2)
print(result3)