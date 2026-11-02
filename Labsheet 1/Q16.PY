# Read dividend and divisor
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

if divisor == 0:
    print("Error: Division by zero is not possible.")
else:
    # Modulus operator gives the remainder
    remainder = dividend % divisor
    print(f"Remainder when {dividend} is divided by {divisor} = {remainder}")