# Update student marks using ID

import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

student_id = int(input("Enter student ID: "))
new_marks = float(input("Enter new marks: "))

cur.execute(
    "UPDATE students SET marks = ? WHERE id = ?",
    (new_marks, student_id)
)

con.commit()

if cur.rowcount > 0:
    print("Marks updated successfully.")
else:
    print("Student not found.")

con.close()