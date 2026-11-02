t = tuple(input("Enter items separated by spaces: ").split())
if not t:
    raise SystemExit("The tuple is empty.")

i = int(input(f"Enter an index (-{len(t)} to {len(t) - 1}): "))
if -len(t) <= i < len(t):
    print(f"Element at index {i} = {t[i]}")
else:
    print("Index out of range.")