t = tuple(input("Enter items separated by spaces: ").split())
if not t:
    raise SystemExit("The tuple is empty.")

print("Original:", t)
print("Reversed:", t[::-1])