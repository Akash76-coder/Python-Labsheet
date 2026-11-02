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

# Bubble sort for ascending order (works on a copy)
ascending = []
for value in numbers:
    ascending.append(value)
n = len(ascending)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if ascending[j] > ascending[j + 1]:
            ascending[j], ascending[j + 1] = ascending[j + 1], ascending[j]

# Descending order = ascending list read from the end
descending = []
for i in range(n - 1, -1, -1):
    descending.append(ascending[i])

print(f"Original   : {numbers}")
print(f"Ascending  : {ascending}")
print(f"Descending : {descending}")