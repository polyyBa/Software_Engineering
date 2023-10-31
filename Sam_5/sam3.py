import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

max_one = max(one)
min_one = min(one)
max_two = max(two)
min_two = min(two)
max_three = max(three)
min_three = min(three)

area1 = (max_one * min_one) / 2
area2 = (max_two * min_two) / 2
area3 = (max_three * min_three) / 2

print("Площадь первого треугольника:", area1)
print("Площадь второго треугольника:", area2)
print("Площадь третьего треугольника:", area3)