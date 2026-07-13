# 6. Write a function to check whether a number is prime.
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n+1):
        if n%i==0:
            return False
    return True
num = int(input("Enter number:"))
if is_prime(num):
    print("prime number")
else:
    print("Not a prime number")    
