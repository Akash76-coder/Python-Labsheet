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

common = []
for value in list1:
    if value in list2 and value not in common:
        common.append(value)

if len(common) == 0:
    print("There are no common elements.")
else:
    print(f"Common elements: {common}")