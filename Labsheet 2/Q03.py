number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Please enter a non-negative integer.")
else:
    # Step 1: count the digits
    temp = number
    digit_count = 0
    if temp == 0:
        digit_count = 1
    while temp > 0:
        digit_count += 1
        temp //= 10

    # Step 2: sum of each digit raised to the power of digit_count
    temp = number
    armstrong_sum = 0
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** digit_count
        temp //= 10

    if armstrong_sum == number:
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is NOT an Armstrong number.")