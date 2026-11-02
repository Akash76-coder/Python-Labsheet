# Delete student record

import sqlite3

con = sqlite3.connect("crud_lab09.db")
cur = con.cursor()

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

con.close()