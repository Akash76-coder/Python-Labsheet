# Update student marks

students = [
    {"roll": 1, "name": "Akash", "marks": 85},
    {"roll": 2, "name": "Rahul", "marks": 90}
]

roll = int(input("Enter roll number: "))
new_marks = int(input("Enter new marks: "))

found = False

for student in students:
    if student["roll"] == roll:
        student["marks"] = new_marks
        found = True
        print("Marks updated successfully.")
        break

if not found:
    print("Student not found.")

print(students)