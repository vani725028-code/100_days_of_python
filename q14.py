# 14. Check whether a number is a Perfect Number.

n = int(input("Enter no.:"))
sum = 0
for i in range(1,n):
    if n%i ==0:
        sum = sum+i
if sum == n:
    print("perfect number") 
else:
    print("Not a perfect number")       