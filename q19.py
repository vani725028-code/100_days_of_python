# 19. Separate even and odd numbers from a list into two different lists.

n = [1,2,8,3,0,1]
even = []
odd = []
for i in n:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)   
print("Even no. is:",even)
print("Odd number is:",odd)        
