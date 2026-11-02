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

# Work on a copy so the original is still shown
reversed_list = []
for value in numbers:
    reversed_list.append(value)

# Swap elements from both ends moving towards the centre
left = 0
right = len(reversed_list) - 1
while left < right:
    reversed_list[left], reversed_list[right] = reversed_list[right], reversed_list[left]
    left += 1
    right -= 1

print(f"Original : {numbers}")
print(f"Reversed : {reversed_list}")