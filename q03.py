# 3. Write a program to find the largest and second largest among three numbers.

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1 >= n2 and n1 >= n3:
    largest = n1
    if n2 >= n3:
        second = n2
    else:
        second = n3

elif n2 >= n1 and n2 >= n3:
    largest = n2
    if n1 >= n3:
        second = n1
    else:
        second = n3

else:
    largest = n3
    if n1 >= n2:
        second = n1
    else:
        second = n2

print("Largest =", largest)
print("Second Largest =", second)
