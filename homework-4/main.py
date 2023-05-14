import math


a = float(input("Введите длину стороны A: "))

b = float(input("Введите длину стороны B: "))

c = float(input("Введите длину стороны C: "))

p = (a+b+c)/2

s = math.sqrt(p*((p-a)*(p-b)*(p-c)))

print("Площадь треугольника = ", s)
