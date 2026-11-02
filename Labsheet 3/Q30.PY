def read_integers(prompt):
    """Read space-separated integers and validate the input."""
    while True:
        numbers = []
        valid = True
        for item in input(prompt).split():
            try:
                numbers.append(int(item))
            except ValueError:
                valid = False
                break
        if valid and numbers:
            return numbers
        print("Invalid input! Enter integers separated by spaces.")


numbers = read_integers("Enter integers separated by spaces: ")

even_numbers = []
odd_numbers = []
for value in numbers:
    if value % 2 == 0:
        even_numbers.append(value)
    else:
        odd_numbers.append(value)

print(f"Original : {numbers}")
print(f"Even     : {even_numbers}")
print(f"Odd      : {odd_numbers}")