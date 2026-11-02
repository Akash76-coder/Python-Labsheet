rows = int(input("Enter number of inner tuples: "))
nested = ()
for i in range(rows):
    nested += (tuple(input(f"Enter items of tuple {i + 1}: ").split()),)
print("Nested tuple:", nested)

r = int(input("Enter inner tuple number: ")) - 1
c = int(input("Enter element position within it: ")) - 1
if 0 <= r < len(nested) and 0 <= c < len(nested[r]):
    print("Element =", nested[r][c])
else:
    print("Position out of range.")