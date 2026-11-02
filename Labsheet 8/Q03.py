# Create students table

import sqlite3

try:
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

    con.commit()

    print("Students table created successfully.")

except Exception as e:
    print("Error:", e)

finally:
    con.close()