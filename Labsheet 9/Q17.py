# Count total student records

import sqlite3

con = sqlite3.connect("crud_lab09.db")
cur = con.cursor()

cur.execute("SELECT COUNT(*) FROM students")

result = cur.fetchone()

print("Total Records:", result[0])

con.close()