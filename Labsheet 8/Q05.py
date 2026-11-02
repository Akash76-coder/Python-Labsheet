# Display all tables

import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("""
    SELECT name FROM sqlite_master
    WHERE type='table'
""")

tables = cur.fetchall()

for table in tables:
    print(table[0])

con.close()