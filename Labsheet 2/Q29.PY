num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 <= 0 or num2 <= 0:
    print("Please enter positive integers.")
else:
    lcm = num1 if num1 > num2 else num2
    # Keep increasing until a number divisible by both is found
    while True:
        if lcm % num1 == 0 and lcm % num2 == 0:
            break
        lcm += 1
    print(f"LCM of {num1} and {num2} = {lcm}")