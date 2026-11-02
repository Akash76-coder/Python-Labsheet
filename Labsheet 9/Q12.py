# Insert student record

import sqlite3

con = sqlite3.connect("crud_lab09.db")
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        marks REAL
    )
""")

cur.execute("""
    INSERT OR IGNORE INTO students
    (id, name, age, marks)
    VALUES (?, ?, ?, ?)
""", (1, "Akash", 22, 85))

con.commit()

print("Student record inserted successfully.")

con.close()