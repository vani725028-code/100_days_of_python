 # 10.  Write a function that merges two lists and removes duplicate elements.
def merge_list(list1,list2):
    merged = list1 + list2
    return list(set(merged))

list1 = [1, 2, 9, 4]
list2 = [3, 9, 5, 2]

print(merge_list(list1, list2))