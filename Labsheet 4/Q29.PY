def read_dict(title):
    """Read a dictionary of text keys and integer values."""
    d = {}
    for _ in range(int(input(f"How many items in {title}? "))):
        key = input("  Key: ")
        d[key] = int(input(f"  Value for {key}: "))
    return d

d1 = read_dict("dictionary 1")
d2 = read_dict("dictionary 2")
common = [key for key in d1 if key in d2]
print("Common keys:", common if common else "None")