number = float(input("Enter a number: "))

# If negative, change the sign (no abs() used)
if number < 0:
    absolute_value = -number
else:
    absolute_value = number

print(f"Absolute value of {number} = {absolute_value}")