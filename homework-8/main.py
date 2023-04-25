
f_number = 0
s_number = int(input("Enter number:  "))

while f_number <= s_number:
    if f_number % 3 == 0:
        print(f_number)
    f_number += 1


fromm = 0
to = int(input("Enter number:  "))
summ = 0

while fromm <= to:
    if fromm % 3 == 0:
        summ += fromm
    fromm += 1
print(f'"Sum of numbers divisible by 3 =  "{summ}')






