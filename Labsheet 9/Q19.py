# Find student with highest marks

import sqlite3

con = sqlite3.connect("crud_lab09.db")
cur = con.cursor()

cur.execute("""
    SELECT * FROM students
    ORDER BY marks DESC
    LIMIT 1
""")

student = cur.fetchone()

if student:
    print("Highest Scoring Student:", student)
else:
    print("No student records found.")

con.close()