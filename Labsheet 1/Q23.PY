number = int(input("Enter an integer: "))

# Remainder 0 when divided by 5 means divisible
if number % 5 == 0:
    print(f"{number} is divisible by 5.")
else:
    print(f"{number} is NOT divisible by 5.")