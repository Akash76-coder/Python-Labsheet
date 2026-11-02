t = tuple(input("Enter items separated by spaces: ").split())
if not t:
    raise SystemExit("The tuple is empty.")

x = input("Enter the element to search: ")
print(f"'{x}' exists in the tuple." if x in t else f"'{x}' does NOT exist in the tuple.")