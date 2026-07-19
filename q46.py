#Write a recursive function to determine whether a string is a palindrome.
def palindrome(n):
    if len(n) <= 1:
        return True
    
    if n[0] != n[-1]:
        return False
    
    return palindrome(n[1:-1])

word = input("Enter string:")
if palindrome(word):
    print("Palindrome")
else:
    print("Not palindrome")      