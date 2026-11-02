t = tuple(input("Enter items separated by spaces: ").split())
if not t:
    raise SystemExit("The tuple is empty.")

x = input("Enter the element to find: ")
if x in t:
    print(f"First index of '{x}' = {t.index(x)}")
else:
    print(f"'{x}' is not in the tuple.")