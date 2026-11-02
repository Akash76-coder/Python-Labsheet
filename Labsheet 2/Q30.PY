number = int(input("Enter a positive integer: "))

if number < 1:
    print("Please enter a positive integer.")
else:
    temp = number
    factorial_sum = 0
    while temp > 0:
        digit = temp % 10
        # Factorial of the digit
        factorial = 1
        for i in range(1, digit + 1):
            factorial *= i
        factorial_sum += factorial
        temp //= 10

    if factorial_sum == number:
        print(f"{number} is a Strong number.")
    else:
        print(f"{number} is NOT a Strong number.")