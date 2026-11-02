number = int(input("Enter an integer: "))

# A multiple of both 3 and 7 leaves remainder 0 for each
if number % 3 == 0 and number % 7 == 0:
    print(f"{number} is a multiple of both 3 and 7.")
else:
    print(f"{number} is NOT a multiple of both 3 and 7.")