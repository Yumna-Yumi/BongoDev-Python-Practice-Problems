list1 = [3, 5, 7, 4, 8, 8]
list2 = [4, 9, 8, 7, 1, 1, 13]

common = list(set(list1) & set(list2))
print("Common items:", common)
print("Sum of common items:", sum(common))