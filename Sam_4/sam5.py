from for_import import geron_formula

a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))

area = geron_formula(a, b, c)

print(f"Площадь треугольника: {area}")