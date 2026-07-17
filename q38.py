# 18. Handle IndexError while accessing list elements

lst = [10, 20, 30, 40]

try:
    index = int(input("Enter the index: "))
    print("Element:", lst[index])

except IndexError:
    print("Error: Index is out of range.")