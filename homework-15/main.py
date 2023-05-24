
import random
import collections

# Task #1

numbers = []

with open("numbers_in_text.txt") as f:
    text = f.read()
    text = text.split()
    for number in text:
        if number.isdigit():
            numbers.append(number)

print(numbers)

# Task #2

user_text = input("Enter your text:  ")
with open("user_text.txt", "w") as t:
    t.write(user_text)

# Task #3

us_numbers = []
numbers_count = input("\nHow many numbers do you want to write?   ")

while not numbers_count.isdigit():
    numbers_count = input("How many numbers do you want to write?   ")

for _number in range(int(numbers_count)):
    user_number = input("Enter your number:  ")
    while not user_number.isdigit():
        user_number = input("Enter your number:  ")
    us_numbers.append(user_number)

with open("numbers.txt", "w") as n:
    n.writelines(" ".join(us_numbers))

# Task 4

random_numbers = []

for _number in range(100):
    random_numbers.append(str(random.randint(1, 1000)))

with open("random_numbers.txt", "w") as r:
    r.writelines("\n".join(random_numbers))

# Task 5

with open("words_count.txt", "r") as c:
    text_c = c.read()

words_count = text_c.split()

print(f'\nFile "words_count.text" has {len(words_count)} words')

# Task 6

with open("sum_of_numbers.txt") as s:
    text_s = s.read().split()
numbers_s_sum = 0
for i in text_s:
    numbers_s_sum += int(i)

print(f'\nThe sum of the numbers in the file '
      f'"sum_of_numbers.txt" is {numbers_s_sum}')

# Task 7

with open("top_words.txt") as t:
    text_t = t.read()

text_t = text_t.split()
text_without_space = "".join(text_t)
top_letters = collections.Counter(text_without_space).most_common(5)

print(f'\nTop 5 letters in the text in file "top_words.txt": '
      f'\n#1 - {top_letters[0]} \n#2 - {top_letters[1]} '
      f'\n#3 - {top_letters[2]} \n#4 - {top_letters[3]} '
      f'\n#5 - {top_letters[4]}')
