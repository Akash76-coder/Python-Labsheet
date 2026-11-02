num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is the largest.")
elif num2 > num1:
    print(f"{num2} is the largest.")
else:
    print("Both numbers are equal.")