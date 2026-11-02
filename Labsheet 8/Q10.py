# Display all student records

import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("SELECT * FROM students")

records = cur.fetchall()

for row in records:
    print(row)

con.close()