number = int(input("Enter an integer: "))

if number < 2:
    # Numbers less than 2 are not prime
    is_prime = False
else:
    is_prime = True
    divisor = 2
    # Only need to test divisors up to the square root of the number
    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor = divisor + 1

if is_prime:
    print(f"{number} is a Prime number.")
else:
    print(f"{number} is NOT a Prime number.")