# Insert multiple student records

import sqlite3

con = sqlite3.connect("student_db.db")
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        marks REAL
    )
""")

data = [
    (2, "Rahul", 23, 90),
    (3, "Mohit", 22, 75),
    (4, "Aman", 24, 88)
]

cur.executemany(
    "INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?)",
    data
)

con.commit()

print("Multiple records inserted successfully.")

con.close()