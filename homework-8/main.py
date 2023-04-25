# a = int(input("from number:  "))
# b = int(input("to number:  "))
# c = a
# d = True if input("even or odd:  ") == "even" else False
# summ = 0
#
# while c <= b:
#     if d and c % 2 == 0:
#         summ += c
#     elif not d and c %  2 == 1:
#         summ += c
#     c += 1
# print(summ)


# a = 0
# b = int(input("number to:  "))
#
# while a <= b:
#     if a % 3 == 0:
#         print(a)
#     a += 1
#
#



f_number = 0
s_number = int(input("Enter number:  "))

while f_number != s_number:
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






