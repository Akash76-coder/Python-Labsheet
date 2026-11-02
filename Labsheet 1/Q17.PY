# Read base and (integer) exponent
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent (integer): "))

# Multiply base repeatedly using a loop instead of pow()
result = 1
count = 0
while count < abs(exponent):
    result = result * base
    count = count + 1

# Negative exponent means reciprocal
if exponent < 0:
    if result == 0:
        print("Error: 0 cannot be raised to a negative power.")
        result = None
    else:
        result = 1 / result

if result is not None:
    print(f"{base} raised to the power {exponent} = {result}")