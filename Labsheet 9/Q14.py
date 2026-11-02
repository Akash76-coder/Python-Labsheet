# Search student by roll number

import sqlite3

con = sqlite3.connect("crud_lab09.db")
cur = con.cursor()

roll = int(input("Enter roll number: "))

cur.execute(
    "SELECT * FROM students WHERE id = ?",
    (roll,)
)

record = cur.fetchone()

if record:
    print("Student Found:", record)
else:
    print("Student not found.")

con.close()