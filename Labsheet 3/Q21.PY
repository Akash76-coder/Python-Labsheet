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

largest = numbers[0]
smallest = numbers[0]
for value in numbers:
    if value > largest:
        largest = value
    if value < smallest:
        smallest = value

print(f"List     : {numbers}")
print(f"Largest  : {largest}")
print(f"Smallest : {smallest}")