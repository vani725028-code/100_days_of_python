# 15. Print a diamond star pattern.

n = int(input("Enter number:"))
for i in range(1,n+1):
    #upper part
    print(" "*(n-i),end = " ")
    print("*" * (2 * i - 1))
    #lower part
for i in range(n-1,0,-1):
    print(" "*(n-i),end = " ")
    print("*"*(2*i-1)) 


    

