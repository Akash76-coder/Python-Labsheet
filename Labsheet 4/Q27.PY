def read_dict(title):
    """Read a dictionary of text keys and integer values."""
    d = {}
    for _ in range(int(input(f"How many items in {title}? "))):
        key = input("  Key: ")
        d[key] = int(input(f"  Value for {key}: "))
    return d

d = read_dict("the dictionary")
result, seen = {}, []
for key in d:
    if d[key] not in seen:     # keep only the first key for each value
        seen.append(d[key])
        result[key] = d[key]
print("Dictionary without duplicate values:", result)