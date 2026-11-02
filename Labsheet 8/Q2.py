# Create a new database

import sqlite3

try:
    con = sqlite3.connect("student_db.db")

    print("Database created successfully.")

except Exception as e:
    print("Error:", e)

finally:
    con.close()
