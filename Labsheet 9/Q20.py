# Student Management System using SQLite

import sqlite3

# Connect to database
con = sqlite3.connect("crud_lab09.db")
cur = con.cursor()

# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        marks REAL
    )
""")

con.commit()


# Add student
def add_student():
    try:
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))

        cur.execute("""
            INSERT INTO students VALUES (?, ?, ?, ?)
        """, (roll, name, age, marks))

        con.commit()

        print("Student added successfully.")

    except ValueError:
        print("Please enter valid numbers.")

    except sqlite3.Error as e:
        print("Error:", e)


# View students
def view_students():
    cur.execute("SELECT * FROM students")

    records = cur.fetchall()

    if records:
        for row in records:
            print(row)
    else:
        print("No records found.")


# Update student
def update_student():
    try:
        roll = int(input("Enter roll number: "))
        marks = float(input("Enter new marks: "))

        cur.execute("""
            UPDATE students SET marks = ?
            WHERE id = ?
        """, (marks, roll))

        con.commit()

        if cur.rowcount > 0:
            print("Student updated successfully.")
        else:
            print("Student not found.")

    except ValueError:
        print("Please enter valid numbers.")


# Delete student
def delete_student():
    try:
        roll = int(input("Enter roll number: "))

        cur.execute(
            "DELETE FROM students WHERE id = ?",
            (roll,)
        )

        con.commit()

        if cur.rowcount > 0:
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    except ValueError:
        print("Enter valid roll number.")


# Main menu
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

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

# Close database
con.close()