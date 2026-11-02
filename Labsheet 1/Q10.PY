# Read temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# F = (C x 9/5) + 32
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius:.2f} C = {fahrenheit:.2f} F")