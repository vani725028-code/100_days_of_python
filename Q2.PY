# 2. Write a program to determine whether a given year is a leap year.

Y = int(input("Enter number:"))
if Y % 400 == 0:
    print("Leap year:",Y)
elif Y % 100 ==0:
    print("Not a Leap year:",Y)
elif Y % 4 ==0:
    print("Leap year:",Y)
else:
    print("Not a Leap year:",Y)        