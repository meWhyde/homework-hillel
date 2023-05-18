
num_files = input("How many files do you want to check:  ")
while not num_files.isdigit():
    num_files = input("How many files do you want to check:  ")

files_library = {}
check_library = {
    "read": "R",
    "write": "W",
    "execute": "X",
}

for i in range(int(num_files)):
    file_name = input(f'Enter name file #{i + 1}:  ')
    name = file_name.strip(" XWR")
    files_library[name] = tuple(file_name.strip(name).split())

files_checks = input("How many checks do you want to run:  ")
while not files_checks.isdigit():
    files_checks = input("How many checks do you want to run:  ")

check_result = ""

for i in range(int(files_checks)):
    print(f"Checking #{i + 1}")
    check_name = input("Enter operation name and file name:  ").split()
    while check_library.get(check_name[0]) is None \
            or files_library.get(check_name[1]) is None:
        check_name = input("Enter correct operation or file name:  ").split()
    if check_library[check_name[0]] in files_library[check_name[1]]:
        check_result += "OK \n"
    else:
        check_result += "Access denied \n"

print(check_result)
