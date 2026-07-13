# 8. Write a function that returns the second largest element of a list.
def second_largest(Ist):
    Ist.sort()
    return Ist[-2]

number = [12,43,87,23]
print("Second largest =",second_largest(number))