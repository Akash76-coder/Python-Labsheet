marks = {}
for _ in range(int(input("How many students? "))):
    name = input("Student name: ")
    marks[name] = float(input(f"Marks of {name}: "))

if not marks:
    print("No data entered.")
else:
    high = low = None
    for name in marks:
        if high is None or marks[name] > marks[high]:
            high = name
        if low is None or marks[name] < marks[low]:
            low = name
    print(f"Maximum: {high} ({marks[high]})")
    print(f"Minimum: {low} ({marks[low]})")