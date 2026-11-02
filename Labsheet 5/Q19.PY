t = tuple(input("Enter items separated by spaces: ").split())
if not t:
    raise SystemExit("The tuple is empty.")

unique = ()
for item in t:
    if item not in unique:       # keep only the first occurrence
        unique += (item,)
print("Original         :", t)
print("Without duplicates:", unique)