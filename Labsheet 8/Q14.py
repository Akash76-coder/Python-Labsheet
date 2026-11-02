# Count student records

import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("SELECT COUNT(*) FROM students")

result = cur.fetchone()

print("Total Students:", result[0])

con.close()