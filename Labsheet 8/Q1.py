# Connect to SQLite database

import sqlite3

try:
    con = sqlite3.connect("student_db.db")

    print("Database connected successfully.")

except Exception as e:
    print("Error:", e)

finally:
    if 'con' in locals():
        con.close()