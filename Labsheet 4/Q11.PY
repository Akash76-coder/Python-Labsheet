marks = {}
for _ in range(int(input("How many students? "))):
    name = input("Student name: ")
    marks[name] = float(input(f"Marks of {name}: "))

print("\nStudent Marks")
for name, mark in marks.items():
    print(f"{name:<15}{mark}")