
my_set = {10, 20, 30, 40}
print("Original set:", my_set)
my_set.discard(20)  # Does not raise an error if element is missing
print("Set after discarding 20:", my_set)