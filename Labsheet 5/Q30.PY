try:
    t1 = tuple(int(x) for x in input("Enter integers of first tuple: ").split())
except ValueError:
    raise SystemExit("Invalid input! Enter integers only.")
if not t1:
    raise SystemExit("The tuple is empty.")
try:
    t2 = tuple(int(x) for x in input("Enter integers of second tuple: ").split())
except ValueError:
    raise SystemExit("Invalid input! Enter integers only.")
if not t2:
    raise SystemExit("The tuple is empty.")

if len(t1) != len(t2):
    print("Both tuples must have the same length.")
else:
    print("Element-wise sum:", tuple(a + b for a, b in zip(t1, t2)))