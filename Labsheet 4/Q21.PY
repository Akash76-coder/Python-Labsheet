def read_dict(title):
    """Read a dictionary of text keys and integer values."""
    d = {}
    for _ in range(int(input(f"How many items in {title}? "))):
        key = input("  Key: ")
        d[key] = int(input(f"  Value for {key}: "))
    return d

d = read_dict("the dictionary")
if not d:
    print("The dictionary is empty.")
else:
    best = None
    for key in d:
        if best is None or d[key] > d[best]:
            best = key
    print(f"Key with maximum value: '{best}' (value = {d[best]})")