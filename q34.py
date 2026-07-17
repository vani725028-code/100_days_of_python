# 14. Sort a list in ascending order without using the sort() method.

list = [3, 8, 4, 9, 2, 6]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] > list[j]:
            list[i],list[j] = list[j],list[i]
            
print("Sorted List:",list)
