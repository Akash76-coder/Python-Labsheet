n = int(input("Enter n: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    total = 0
    # Add 1 + 2 + ... + n
    for i in range(1, n + 1):
        total += i
    print(f"Sum of first {n} natural numbers = {total}")