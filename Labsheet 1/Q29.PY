# Read the range limits and the number to check
lower_limit = float(input("Enter the lower limit: "))
upper_limit = float(input("Enter the upper limit: "))
number = float(input("Enter the number to check: "))

# Chained comparison checks both limits (inclusive)
if lower_limit <= number <= upper_limit:
    print(f"{number} lies within the range [{lower_limit}, {upper_limit}].")
else:
    print(f"{number} lies outside the range [{lower_limit}, {upper_limit}].")