
a = input("Enter value of a: ")
b = input("Enter value of b: ")
print(f"Before swapping: a = {a}, b = {b}")

# Swap using a temporary variable
temp = a
a = b
b = temp

print(f"After swapping:  a = {a}, b = {b}")