t = tuple(input("Enter strings separated by spaces: ").split())
if not t:
    raise SystemExit("The tuple is empty.")

print("Sorted tuple:", tuple(sorted(t, key=str.lower)))     # case-insensitive order