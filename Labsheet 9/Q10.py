# CRUD operations using text file

import json
import os

filename = "student_records.json"

# Read records from file
def read_data():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []


# Add student
def add_student():
    students = read_data()

    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = input("Enter marks: ")

    for student in students:
        if student["roll"] == roll:
            print("Roll number already exists.")
            return

    students.append({
        "roll": roll,
        "name": name,
        "marks": marks
    })

    with open(filename, "w") as file:
        json.dump(students, file)

    print("Record added successfully.")


# View students
def view_students():
    students = read_data()

    for student in students:
        print(student)


# Update student
def update_student():
    students = read_data()

    roll = input("Enter roll number: ")

    for student in students:
        if student["roll"] == roll:
            student["marks"] = input("Enter new marks: ")

            with open(filename, "w") as file:
                json.dump(students, file)

            print("Record updated successfully.")
            return

    print("Student not found.")


# Delete student
def delete_student():
    students = read_data()

    roll = input("Enter roll number: ")

    new_students = [
        student for student in students
        if student["roll"] != roll
    ]

    if len(new_students) == len(students):
        print("Student not found.")
    else:
        with open(filename, "w") as file:
            json.dump(new_students, file)

        print("Record deleted successfully.")


# Main menu
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")

    except (ValueError, OSError, json.JSONDecodeError) as e:
        print("Error:", e)