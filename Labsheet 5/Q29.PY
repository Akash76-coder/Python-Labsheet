t = tuple(input("Enter items separated by spaces: ").split())
if not t:
    raise SystemExit("The tuple is empty.")

print("All elements are the same." if t.count(t[0]) == len(t) else "Elements are NOT all the same.")