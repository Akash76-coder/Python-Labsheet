number = int(input("Enter an integer: "))

if number < 0:
    number = -number

original = number
digit_sum = 0
while number > 0:
    digit_sum += number % 10   # add last digit
    number //= 10              # drop last digit

print(f"Sum of digits of {original} = {digit_sum}")