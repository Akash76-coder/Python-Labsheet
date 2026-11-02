# Connect database and create students table

import sqlite3

try:
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

    con.commit()

    print("Students table created successfully.")

except sqlite3.Error as e:
    print("Database Error:", e)

finally:
    con.close()