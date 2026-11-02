number = int(input("Enter an integer: "))

is_negative = number < 0
if is_negative:
    number = -number

original = number
reversed_number = 0
while number > 0:
    digit = number % 10                       # last digit
    reversed_number = reversed_number * 10 + digit
    number //= 10                             # remove last digit

if is_negative:
    reversed_number = -reversed_number
    original = -original

print(f"Reverse of {original} = {reversed_number}")