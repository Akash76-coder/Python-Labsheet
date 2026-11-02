t = tuple(input("Enter items separated by spaces: ").split())
if not t:
    raise SystemExit("The tuple is empty.")

print("Tuple :", t)
print("Length:", len(t))