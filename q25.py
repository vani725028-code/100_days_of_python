# 5. Remove empty strings and strings containing only spaces from a list using list comprehension.

words = ["apple", "", "banana", "   ", "mango", "orange", "  "]

new_list = []

for i in words:
    if i.strip():
        new_list.append(i)

print(new_list)