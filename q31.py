# 11. Find the common elements between two lists without using sets.
list1 = [2,6,3,4,1]
list2 = [2,3,0,5,6,5]
for i in list1:
    for j in list2:
        if i ==j:
            print(i)

# second method
list1 = [2,6,3,4,1]
list2 = [2,3,0,5,6,5]

common =[]
for i in list1:
    for j in list2:
        if i ==j:
            common.append(i)
print(common)
                     
