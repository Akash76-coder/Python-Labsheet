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

elements = []
counts = []
for value in numbers:
    position = -1
    for i in range(len(elements)):
        if elements[i] == value:
            position = i
            break
    if position == -1:
        elements.append(value)
        counts.append(1)
    else:
        counts[position] += 1

print("Element frequencies:")
for i in range(len(elements)):
    print(f"  {elements[i]} : {counts[i]}")