# Read dividend and divisor
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

# Division by zero is not allowed
if divisor == 0:
    print("Error: Division by zero is not possible.")
else:
    quotient = dividend // divisor   # floor (integer) division
    remainder = dividend % divisor   # modulus operator
    print(f"Quotient  = {quotient}")
    print(f"Remainder = {remainder}")