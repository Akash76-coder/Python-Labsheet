# Delete student record

students = [
    {"roll": 1, "name": "Akash", "marks": 85},
    {"roll": 2, "name": "Rahul", "marks": 90},
    {"roll": 3, "name": "Mohit", "marks": 75}
]

roll = int(input("Enter roll number: "))

found = False

for student in students:
    if student["roll"] == roll:
        students.remove(student)
        found = True
        print("Student deleted successfully.")
        break

if not found:
    print("Student not found.")

print("Remaining Records:", students)