# 12. Find the missing number from a list containing numbers from 1 to N.

number =[1,2,4,5,7,8]
n = 8
for i in range(1,n+1):
    if i not in number:
        print("Missing number is:",i)