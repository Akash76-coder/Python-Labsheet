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

largest = None
second_largest = None
for value in numbers:
    if largest is None or value > largest:
        second_largest = largest     # old largest becomes second largest
        largest = value
    elif value != largest and (second_largest is None or value > second_largest):
        second_largest = value

if second_largest is None:
    print("There is no second largest element (need at least two distinct values).")
else:
    print(f"Largest        : {largest}")
    print(f"Second largest : {second_largest}")