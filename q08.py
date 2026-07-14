# 8. Check whether a string is a palindrome using slicing.

s =input('Enter string:')

if s== s[::-1]:
    print('palindrome')
else:
    print('not a palindrome')




#second way 

    s =input('Enter string:')

reverse = s[::-1]

if s==reverse:

    print('palindrome')

else:

    print('not a palindrome')