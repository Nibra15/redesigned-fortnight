list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 16, 1, 3, 8, 2]

set1 = set(list1)
set2 = set(list2)
set1.update(set2)
set1.intersection_update(set2)


print(set1)
