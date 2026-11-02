t = tuple(input("Enter items separated by spaces: ").split())
if not t:
    raise SystemExit("The tuple is empty.")

repeated = ()
for item in t:
    if t.count(item) > 1 and item not in repeated:
        repeated += (item,)
print("Repeated items:", repeated if repeated else "None")