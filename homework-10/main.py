
"""
Lor3333e4m 34 23 ipsum dol23or sit amet, 234 234 34 co234nsectetur adipisci234ng eli234t,

Lorem ipsum dolor sit amet, consectetur adipiscing elit,
"""

polin = input("Enter palindrome word:  ")

if polin == polin[::-1]:
    print("+")
else:
    print("-")



text_all = input("Enter your text:  ")
search = input("Enter a search word:  ")
answer = "NO"
clean = ""

for i in text_all:
    if i.isalnum() or i.isspace():
        clean += i

clean = clean.split()

for i in clean:
    if i.lower() == search.lower():
        answer = "YES"

print(answer)



text_rap = input("Enter your text:  ")

if text_rap.find("abc") == 0:
    text_rap = text_rap.replace("abc", "www", 1)
else:
    text_rap += "qqq"

print(text_rap)



text_num = input("Enter your text:  ")
text_with = ""
text_fin = ""

for i in text_num:
    if not i.isdigit():
        text_with += i
text_with = text_with.split()

for i in text_with:
    text_fin += i + " "

print(text_fin)



mail = input("Enter your email:  ")

while len(mail) <= 6:
    mail = input("Enter your email again:  ")

if mail.find("@") != -1 and mail.find(".") != -1:
    print("YES")
else:
    print("NO")