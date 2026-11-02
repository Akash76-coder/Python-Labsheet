number = int(input("Enter an integer: "))

if number < 0:
    number = -number

if number == 0:
    count = 1
else:
    count = 0
    temp = number
    # Remove one digit at a time and count
    while temp > 0:
        count += 1
        temp //= 10

print(f"Number of digits in {number} = {count}")