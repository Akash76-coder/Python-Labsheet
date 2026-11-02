year = int(input("Enter a year: "))

# Leap year: divisible by 4 and not by 100, OR divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is NOT a Leap Year.")