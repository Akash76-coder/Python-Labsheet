number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Please enter a non-negative integer.")
else:
    original = number
    reversed_number = 0

    # Build the reverse of the number digit by digit
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    if original == reversed_number:
        print(f"{original} is a Palindrome.")
    else:
        print(f"{original} is NOT a Palindrome.")