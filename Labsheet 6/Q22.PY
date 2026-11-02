
my_list = [1, 2, 3, 2, 4, 5, 3, 6]
seen = set()
duplicates = set()
for item in my_list:
  if item in seen:
    duplicates.add(item)
  else:
    seen.add(item)
print("Original list:", my_list)
print("Duplicate elements:", duplicates)