# Read two numbers
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print(f"Before swapping: a = {a}, b = {b}")

# Swap using arithmetic operations (no temporary variable)
a = a + b
b = a - b   # b now holds the original a
a = a - b   # a now holds the original b

print(f"After swapping:  a = {a}, b = {b}")
