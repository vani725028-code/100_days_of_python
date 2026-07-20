#  Read numbers until 'stop' is entered, handle invalid inputs using try-except, then calculate minimum, maximum, average, and median.
numbers = []

while True:
    value = input("Enter a number (or 'stop' to finish): ")

    if value.lower() == "stop":
        break

    try:
        num = float(value)
        numbers.append(num)

    except ValueError:
        print("Invalid input! Please enter a valid number.")

if len(numbers) == 0:
    print("No numbers entered.")

else:
    numbers.sort()

    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    if len(numbers) % 2 == 1:
        median = numbers[len(numbers) // 2]
    else:
        mid = len(numbers) // 2
        median = (numbers[mid - 1] + numbers[mid]) / 2

    print("Minimum =", minimum)
    print("Maximum =", maximum)
    print("Average =", average)
    print("Median =", median)