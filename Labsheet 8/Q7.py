# Check if students table exists

import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("""
    SELECT name FROM sqlite_master
    WHERE type='table' AND name='students'
""")

result = cur.fetchone()

if result:
    print("Students table exists.")
else:
    print("Students table does not exist.")

con.close()