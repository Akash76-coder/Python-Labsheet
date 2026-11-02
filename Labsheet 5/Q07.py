t = tuple(input("Enter items separated by spaces: ").split())
if not t:
    raise SystemExit("The tuple is empty.")

x = input("Enter the element to count: ")
print(f"'{x}' occurs {t.count(x)} time(s).")