print("Prime numbers between 1 and 100:")
for number in range(2, 101):
    is_prime = True
    # Test divisors up to the square root of number
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        print(number, end=" ")
print()