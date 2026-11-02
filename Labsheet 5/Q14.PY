def parse(token):
    """Return int/float for numeric tokens, otherwise the text itself."""
    for kind in (int, float):
        try:
            return kind(token)
        except ValueError:
            pass
    return token

t = tuple(parse(x) for x in input("Enter items (numbers and text mixed): ").split())
total = 0
for item in t:
    if isinstance(item, (int, float)):     # ignore non-numeric items
        total += item
print("Tuple :", t)
print("Sum of numeric elements =", total)