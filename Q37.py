# 17. Accept integer input until a valid integer is entered using try-except.
while True:
    try:
        num = int(input("Enter number:"))
        print("YOU entered:",num)
        break
    except ValueError:
        print("Invalid input!Please enter a valid integer.")