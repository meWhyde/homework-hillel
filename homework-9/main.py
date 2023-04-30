
password = input("Please enter your password:  ")

lover = 0
upper = 0
number = 0
symbol = 0
words = 0

if len(password) >= 8:
    words = 1
if not password.find(" ") == -1:
    print("Don't use space in password!")
    exit()

for pas in password:
    if pas.islower():
        lover = 1
    elif pas.isupper():
        upper = 1
    elif pas.isdigit():
        number = 1
    elif not pas.isalnum():
        symbol = 1

summ = lover + upper + number + words + symbol

print(f'Pasword socer: {summ}')

if words == 0:
    print("The minimum password length is 8")
if lover == 0:
    print("Use lower letters in password!")
if upper == 0:
    print("Use upper letters in password!")
if number == 0:
    print("Use digits in password!")
if symbol == 0:
    print("Use special characters in password!")

