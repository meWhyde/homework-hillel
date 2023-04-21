# a = int(input("month"))
#
# b = int(input("day"))
#
# if a > 12 and a < 1 or b < 1 and b > 31:
#     print("no corect month or day")
#
#
# if a == 1 and b >= 20 or a == 2 and b <= 18:
#     print("vodoley")
#
# if a == 2 and b >= 19 and b <= 29 or a == 3 and b <= 20:
#     print("ryba")
# elif a == 2 and b > 29:
#     print("no corect month or day")
#
# if a == 3 and b >= 21 or a == 4 and b <= 19:
#     print("oven")
#
# if a == 4 and b >= 20 or a == 5 and b <= 20:
#     print("telec")
#
# if a == 5 and b >= 21 or a == 6 and b <= 22:
#     print("blizhec")
#
# if a == 6 and b >= 23 or a == 7 and b <= 22:
#     print("rak")
#
# if a == 7 and b >= 23 or a == 8 and b <= 22:
#     print("lev")
#
# if a == 8 and b >= 23 or a == 9 and b <= 22:
#     print("deva")
#
# if a == 9 and b >= 23 or a == 10 and b <= 22:
#     print("vesy")
#
# if a == 10 and b >= 23 or a == 11 and b <= 21:
#     print("skorpion")
#
# if a == 11 and b >= 22 or a == 12 and b <= 21:
#     print("strilec")
#
# if a == 12 and b >= 22 or a == 1 and b <= 19:
#     print("kozerog")


# a = int(input("enter number"))
#
# if a % 2 == 0:
#     print("even")


day = int(input("enter day of your birthday"))

month = int(input("enter month of your birthday 1-12"))

feb = day >= 20 and day <= 29


if month == 2 and day >= 20 and day <= 29 or month == 3 and day <= 18:
     print("vodoley")



if month == 2 and day >= 20 and day <= 29:
    print("vodoley")
elif month == 3 and day <= 18:
    print("vodoley")



if month == 2 and feb or month == 3 and day <= 18:
    print("vodoley")





