try:
    t = tuple(int(x) for x in input("Enter integers separated by spaces: ").split())
except ValueError:
    raise SystemExit("Invalid input! Enter integers only.")
if not t:
    raise SystemExit("The tuple is empty.")

print("Sorted tuple:", tuple(sorted(t)))