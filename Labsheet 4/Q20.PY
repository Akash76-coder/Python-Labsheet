def read_dict(title):
    """Read a dictionary of text keys and integer values."""
    d = {}
    for _ in range(int(input(f"How many items in {title}? "))):
        key = input("  Key: ")
        d[key] = int(input(f"  Value for {key}: "))
    return d

d = read_dict("the dictionary")
total = 0
for key in d:
    total += d[key]
print("Sum of all values =", total)