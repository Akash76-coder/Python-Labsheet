# Read temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# C = (F - 32) x 5/9
celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit:.2f} F = {celsius:.2f} C")