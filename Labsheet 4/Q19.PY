def read_dict(title):
    """Read a dictionary of text keys and integer values."""
    d = {}
    for _ in range(int(input(f"How many items in {title}? "))):
        key = input("  Key: ")
        d[key] = int(input(f"  Value for {key}: "))
    return d

d = read_dict("the dictionary")
key = input("Enter the key to search: ")
print(f"Key '{key}' exists." if key in d else f"Key '{key}' does NOT exist.")