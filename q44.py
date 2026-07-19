# 4. Reverse a string using recursion.
def reverse(n):
    if len(n)==0 or len(n)==1:
        return n
    else:
        return reverse(n[1:]) + n[0]
sentence = input("Enter string:")
print("Reverse",reverse(sentence))
