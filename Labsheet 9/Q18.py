# Sort student records by name

import sqlite3

con = sqlite3.connect("crud_lab09.db")
cur = con.cursor()

cur.execute("SELECT * FROM students ORDER BY name ASC")

records = cur.fetchall()

for row in records:
    print(row)

con.close()