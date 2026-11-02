t = tuple(input("Enter items separated by spaces: ").split())
if not t:
    raise SystemExit("The tuple is empty.")

n = int(input("Enter n: "))
print(f"Tuple repeated {n} times:", t * n)