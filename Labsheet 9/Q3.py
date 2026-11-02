# Search student by name

students = [
    {"roll": 1, "name": "Akash", "marks": 85},
    {"roll": 2, "name": "Rahul", "marks": 90},
    {"roll": 3, "name": "Mohit", "marks": 75}
]

name = input("Enter student name: ")

found = False

for student in students:
    if student["name"].lower() == name.lower():
        print("Student Found:", student)
        found = True
        break

if not found:
    print("Student not found.")