# 19. Handle FileNotFoundError while opening a file.

try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: File not found.")