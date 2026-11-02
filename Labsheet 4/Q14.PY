def read_dict(title):
    """Read a dictionary of text keys and integer values."""
    d = {}
    for _ in range(int(input(f"How many items in {title}? "))):
        key = input("  Key: ")
        d[key] = int(input(f"  Value for {key}: "))
    return d

d1 = read_dict("dictionary 1")
d2 = read_dict("dictionary 2")
merged = {}
for key in d1:
    merged[key] = d1[key]
for key in d2:
    merged[key] = d2[key]      # for a common key, dictionary 2's value is kept
print("Merged dictionary:", merged)