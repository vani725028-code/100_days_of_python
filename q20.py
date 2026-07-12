# 20. Rotate a list by K positions to the left.

n = [1,2,8,3,0,1]
K = int(input("Enter k:"))
result = n[K:] + n[:K]
print(result)