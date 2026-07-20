# Use list comprehension and a helper function to create a list containing only prime numbers.
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

prime_list = [i for i in numbers if is_prime(i)]

print("Prime Numbers:", prime_list)