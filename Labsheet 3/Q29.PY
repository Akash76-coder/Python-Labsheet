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

# Elements present in list1 but not in list2
only_in_first = []
for value in list1:
    if value not in list2 and value not in only_in_first:
        only_in_first.append(value)

# Elements present in list2 but not in list1
only_in_second = []
for value in list2:
    if value not in list1 and value not in only_in_second:
        only_in_second.append(value)

print(f"List1 - List2 : {only_in_first}")
print(f"List2 - List1 : {only_in_second}")