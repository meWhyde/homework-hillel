#
# first_list = []
#
# for i in range(5):
#     tmp = input(f'Enter #{i + 1} number:  ')
#     while not tmp.lstrip("-").isdigit():
#         tmp = input(f'Enter #{i + 1} number:  ')
#     first_list.append(int(tmp))
#
# print(f'\n{first_list}\n')


#
# second_list = [1, 2, 3, 4, 5,]
# second_list.pop()
# print(f'{second_list}\n')
#
#
#
# third_list = []
#
# for i in range(10):
#     tmp = input(f'Enter #{i + 1} number: ')
#     while not tmp.lstrip("-").isdigit():
#         tmp = input(f'Enter #{i + 1} number: ')
#     third_list.append(int(tmp))
#
# search_number = input(f'\nWhat number are you looking:  ')
# while not search_number.lstrip("-").isdigit():
#      search_number = input(f'What number are you looking: ')
#
# sum_numbers = third_list.count(int(search_number))
#
# print(f'\nThis list have {sum_numbers} numbers {search_number}\n')


#
# sum_numbers = input("\nHow many numbers do you want to list:  ")
# while not sum_numbers.isdigit():
#     sum_numbers = input("How many numbers do you want to list:  ")
# fourth_list = []
#
# for i in range(int(sum_numbers)):
#     tmp = input(f'Enter #{i + 1} number: ')
#     while not tmp.lstrip("-").isdigit():
#         tmp = input(f'Enter #{i + 1} number: ')
#     fourth_list.append(int(tmp))
#
# fourth_list.reverse()
# print(f'\n{fourth_list}\n')


# fifth_list = []
# fifth_big_list = []
#
# for i in range(5):
#     tmp = input(f'Enter #{i + 1} number: ')
#     while not tmp.lstrip("-").isdigit():
#         tmp = input(f'Enter #{i + 1} number: ')
#     fifth_list.append(int(tmp))
#
# for i in fifth_list:
#     if i > 5:
#         fifth_big_list.append(i)
#
# if len(fifth_big_list) == 0:
#     print(f'\nAll your numbers are less than 6')
# else:
#     print(f'\n{fifth_big_list}\n')
#
#
# sixth_list_sum = input("\nHow many numbers do you want to list:  ")
# while not sixth_list_sum.isdigit() or int(sixth_list_sum) == 0:
#     sixth_list_sum = input("How many numbers do you want to list:  ")
#
# sixth_list = []
#
# for i in range(int(sixth_list_sum)):
#     tmp = input(f'Enter #{i + 1} number: ')
#     while not tmp.lstrip("-").isdigit():
#         tmp = input(f'Enter #{i + 1} number: ')
#     sixth_list.append(int(tmp))
#
# sixth_list_max = sixth_list[0]
# sixth_list_min = sixth_list[0]
#
# for i in sixth_list:
#     if i > sixth_list_max:
#         sixth_list_max = i
#     if i < sixth_list_min:
#         sixth_list_min = i
#
# print(f'\nThe minimum number in the list {sixth_list_min}, and the maximum number in list {sixth_list_max}\n')

#

seventh_list = []
text_numbers = input("Enter your text:  ")

for i in text_numbers:
    if i.isdigit():
        seventh_list.append(int(i))
print(f'\n{len(seventh_list)} digits in your text')
