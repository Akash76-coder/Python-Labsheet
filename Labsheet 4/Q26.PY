def read_dict(title):
    """Read a dictionary of text keys and integer values."""
    d = {}
    for _ in range(int(input(f"How many items in {title}? "))):
        key = input("  Key: ")
        d[key] = int(input(f"  Value for {key}: "))
    return d

d1 = read_dict("dictionary 1")
d2 = read_dict("dictionary 2")
# Equal when they have the same keys and every key has the same value
equal = len(d1) == len(d2)
for key in d1:
    if key not in d2 or d1[key] != d2[key]:
        equal = False
print("The dictionaries are EQUAL." if equal else "The dictionaries are NOT equal.")