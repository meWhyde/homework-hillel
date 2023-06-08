
# Task 1
change_list = [1, "Well", None, 909, "Hello", False]


def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


print(change(change_list))

# Task 2
list_to_dict = [1, "Hello", 23, "Bob", "John", 999]


def to_dict(lst: list):
    final_dict = {}
    for i in lst:
        final_dict[i] = i
    return final_dict


print(to_dict(list_to_dict))

# Task 3
start_number = input("Enter first number:  ")
while not start_number.isdigit():
    start_number = input("Enter first number:  ")

end_number = input("Enter second number:  ")
while not end_number.isdigit():
    end_number = input("Enter second number:  ")

sum_range_list = []
sum_range_list.append(int(start_number))
sum_range_list.append(int(end_number))
sum_range_list = sorted(sum_range_list)


def sum_range(start, end):
    sum_range = 0
    for i in range(start, end + 1):
        sum_range += i
    return sum_range


print(sum_range(sum_range_list[0], sum_range_list[1]))
