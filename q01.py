# 1. Write a program to input marks in five subjects and calculate the total, percentage, and grade.

m1 = int(input("Enter a marks in eng:"))
m2 = int(input("Enter a marks in math:"))
m3 = int(input("Enter a marks in sci:"))
m4 = int(input("Enter a marks in sst:"))
m5 = int(input("Enter a marks in hindi:"))

Total = m1 + m2 + m3 + m4 + m5
print('Total marks',Total)

percentage = (Total/500)*100
print('percentage=',percentage)

if percentage >= 80:
    print('Grade : EXELLENT')
elif percentage >= 60:
    print('Grade : GOOD')
elif percentage >= 40:
    print('Grade : WORK HARD')
else:
    print('Grade:False')

