# Update student name

import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

student_id = int(input("Enter student ID: "))
new_name = input("Enter new name: ")

cur.execute(
    "UPDATE students SET name = ? WHERE id = ?",
    (new_name, student_id)
)

con.commit()

if cur.rowcount > 0:
    print("Name updated successfully.")
else:
    print("Student not found.")

con.close()