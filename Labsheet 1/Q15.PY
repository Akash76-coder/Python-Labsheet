# 1 kilometer = 0.621371 miles
CONVERSION_FACTOR = 0.621371

kilometers = float(input("Enter distance in kilometers: "))
miles = kilometers * CONVERSION_FACTOR

print(f"{kilometers:.2f} km = {miles:.2f} miles")