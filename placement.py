import sqlite3

def add_student():

    conn = sqlite3.connect("campus.db")
    cursor = conn.cursor()

    name = input("Name: ")
    department = input("Department: ")
    cgpa = float(input("CGPA: "))
    skills = input("Skills: ")
    phone = input("Phone: ")
    email = input("Email: ")

    cursor.execute("""
    INSERT INTO students
    (name,department,cgpa,skills,phone,email)
    VALUES(?,?,?,?,?,?)
    """,
    (name,department,cgpa,
     skills,phone,email))

    conn.commit()
    conn.close()

    print("Student Added")

add_student()
