
files_sum = int(input("How many files do you want to check:  "))
files = {}

for i in range(files_sum):
    print(f'Enter name file #{i + 1}:  ')
    file_name = input("Enter file name:  ")
    name = file_name.strip(" XWR")
    files["read " + name] = "Access denied"
    files["write " + name] = "Access denied"
    files["execute " + name] = "Access denied"
    if file_name.find(" X") != -1:
        files["execute " + name] = "OK"
    if file_name.find(" W") != -1:
        files["write " + name] = "OK"
    if file_name.find(" R") != -1:
        files["read " + name] = "OK"

check_sum = int(input("How many file checks:  "))
final_answer = ""

for i in range(check_sum):
    checking = files[input(f'Write the name of the file #{i + 1} to check:  ')]
    final_answer += checking + "\n"

print(final_answer)
