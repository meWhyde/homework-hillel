
a = int(input("Введите длину стороны A: "))

b = int(input("Введите длину стороны B: "))

c = int(input("Введите длину стороны C: "))

p = (a+b+c)/2

print("Площадь треугольника = ", (p*((p-a)*(p-b)*(p-c))) **(0.5))



