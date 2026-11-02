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

unique = []
for value in numbers:
    if value not in unique:    # keep only the first occurrence
        unique.append(value)

print(f"Original         : {numbers}")
print(f"Without duplicates: {unique}")