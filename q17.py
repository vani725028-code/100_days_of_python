# 17. Remove duplicate elements from a list while maintaining the original order.

n = [10,20,30,20,75,25]
new_list = []
for i in n:
    if i not in new_list:
        new_list.append(i)
print(new_list)        