number = int(input("Enter a positive integer: "))

if number < 1:
    print("Please enter a positive integer.")
else:
    # Sum of proper divisors (all divisors except the number itself)
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i

    if divisor_sum == number:
        print(f"{number} is a Perfect number.")
    else:
        print(f"{number} is NOT a Perfect number.")