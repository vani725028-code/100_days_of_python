# 9. Find the frequency of each character in a string.
n = input("Enter number:")
checked = ""
for i in n:
    if i not in checked:
        print(i,":",n.count(i))
        checked = checked + i



 