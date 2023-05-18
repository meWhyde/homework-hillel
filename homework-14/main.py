
juni_debtors = {
    "Oliver", "Jack", "Noah",
    "Liam", "Mason", "James",
    "Benjamin", "Emma", "Ava",
    "Isabella", "Emily", "Mia",
    "Ethan", "Abigail",
}
juli_debtors = {
    "Oliver", "Jack", "Noah",
    "James", "Benjamin", "Jacob",
    "Michael", "Elijah", "Ethan",
    "Emma", "Olivia", "Ava",
    "Charlotte", "Abigail", "Emily",
    "Harper",
}

print(f'\nDues for june and july: \n{juni_debtors.intersection(juli_debtors)}')
print(f'\nDues for july: \n{juli_debtors.difference(juni_debtors)}')

camel_list = ["FirstItem", "FriendsList", "MyTuple"]
snake_list = []

for i in range(len(camel_list)):
    snake_case = ""
    for word in camel_list[i]:
        if word.isupper():
            snake_case += "_"
        snake_case += word.lower()
    snake_list.append(snake_case.lstrip("_"))

print("\n", snake_list)
