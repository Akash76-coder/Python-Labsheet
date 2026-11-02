number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    # n! = 1 x 2 x ... x n  (0! = 1)
    for i in range(1, number + 1):
        factorial *= i
    print(f"Factorial of {number} = {factorial}")