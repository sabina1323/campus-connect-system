import sqlite3

conn = sqlite3.connect("campus.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    cgpa REAL,
    skills TEXT,
    phone TEXT,
    email TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS companies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    required_cgpa REAL,
    required_skill TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS hostel(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT,
    room_no TEXT,
    block_name TEXT,
    fee_status TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")
