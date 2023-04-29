
number_1 = int(input("Enter number:  "))
star_1 = "*"
for stars in range(0, number_1):
    print(star_1 * number_1)
    number_1 -= 1

number_2 = int(input("Enter number:  "))
star_2 = "*"
for stars in range(0, number_2):
    print(star_2)
    star_2 += "*"

number_3 = int(input("Enter number:  "))
star_3 = "*"
space = ""
for stars in range(0, number_3):
    print(f'{space}{star_3 * number_3}')
    space += " "
    number_3 -= 1

number_4 = int(input("Enter number:  "))
star_4 = "*"
for stars in range(0, number_4):
    number_4 -= 1
    print(f'{" " * number_4}{star_4}')
    star_4 += "*"