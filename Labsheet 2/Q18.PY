n = int(input("Enter number of terms: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    first, second = 0, 1
    print(f"Fibonacci series ({n} terms):")
    for _ in range(n):
        print(first, end=" ")
        # Next term is the sum of the previous two
        first, second = second, first + second
    print()