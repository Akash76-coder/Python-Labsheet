# Update student marks

import sqlite3

con = sqlite3.connect("crud_lab09.db")
cur = con.cursor()

roll = int(input("Enter roll number: "))
marks = float(input("Enter new marks: "))

cur.execute(
    "UPDATE students SET marks = ? WHERE id = ?",
    (marks, roll)
)

con.commit()

if cur.rowcount > 0:
    print("Marks updated successfully.")
else:
    print("Student not found.")

con.close()