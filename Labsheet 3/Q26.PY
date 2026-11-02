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


list1 = read_integers("Enter elements of first list (space separated): ")
list2 = read_integers("Enter elements of second list (space separated): ")

merged = []
for value in list1:
    merged.append(value)
for value in list2:
    merged.append(value)

print(f"List 1 : {list1}")
print(f"List 2 : {list2}")
print(f"Merged : {merged}")