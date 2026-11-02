num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 <= 0 or num2 <= 0:
    print("Please enter positive integers.")
else:
    smaller = num1 if num1 < num2 else num2
    hcf = 1
    # Check every candidate from 1 up to the smaller number
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i      # last common divisor found is the HCF
    print(f"HCF of {num1} and {num2} = {hcf}")