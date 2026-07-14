# 6. Input a string and print the first 3 characters, last 3 characters, every alternate character, and the reversed string.

n = input('Enter string:')
p = n[:3]
print(p)
q = n[:-4:-1]
print(q)
a = n[::2]
print(a)
l = n[::-1]
print(l)