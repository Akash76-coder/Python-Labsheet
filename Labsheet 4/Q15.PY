def read_dict(title):
    """Read a dictionary of text keys and integer values."""
    d = {}
    for _ in range(int(input(f"How many items in {title}? "))):
        key = input("  Key: ")
        d[key] = int(input(f"  Value for {key}: "))
    return d
def sort_items(items, pos):
    """Insertion sort of (key, value) pairs by position pos (0=key, 1=value)."""
    for i in range(1, len(items)):
        cur, j = items[i], i - 1
        while j >= 0 and items[j][pos] > cur[pos]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = cur
    return items

d = read_dict("the dictionary")
print("Sorted by keys:", dict(sort_items(list(d.items()), 0)))