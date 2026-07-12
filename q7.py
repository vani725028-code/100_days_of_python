# 7. Count the number of vowels, consonants, digits, and special characters in a string.

n = input('Enter string:')
vowel = 0
consonant = 0
digit = 0
special = 0

for w in n:
    if w in"AEIOUaeiou":
        vowel+=1
    elif w.isalpha():
        consonant+=1
    elif w.isdigit():
        digit+=1
    else:
        special+=1
print("Vowels =", vowel)
print("Consonants =", consonant)
print("Digits =", digit)
print("Special Characters =", special)
