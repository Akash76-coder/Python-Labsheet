
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4}
print("Original Set 1:", set1)
print("Set 2 to remove:", set2)
set1.difference_update(set2)
print("Set 1 after removing elements of Set 2:", set1)