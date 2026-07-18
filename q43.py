#3. Find the sum of digits of a number using recursion.
def sum_digit(n):
    if n ==0:
        return 0
    else:
        return (n%10)+sum_digit(n//10)
num = int(input("Enter no.:"))
print("sum of digits =",sum_digit(num))