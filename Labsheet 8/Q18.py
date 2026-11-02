# Delete student using ID

import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

student_id = int(input("Enter student ID: "))

cur.execute(
    "DELETE FROM students WHERE id = ?",
    (student_id,)
)

con.commit()

if cur.rowcount > 0:
    print("Student deleted successfully.")
else:
    print("Student not found.")

con.close()