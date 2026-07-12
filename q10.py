# 10. Remove all spaces from a string and count the number of words.

n = input("Enter number:")

new = n.replace(' ','')
print("string without spaces:",new)

word = n.split()
print("Number of words:",len(word))