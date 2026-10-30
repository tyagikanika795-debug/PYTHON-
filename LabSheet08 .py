# LAB SHEET - 08
# Python Programming Lab: Database Management using Python
# MCA I Semester | Session 2026-2027
# Simple SQLite programs. Run this file and select a program from the menu.

import sqlite3
import csv

DB = "student.db"

def connect():
    return sqlite3.connect(DB)

def program_1():
    con = connect()
    print("Database connected successfully")
    con.close()

def program_2():
    con = sqlite3.connect("student.db")
    print("Database created successfully")
    con.close()

def program_3():
    con = connect()
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER, name TEXT, age INTEGER, marks INTEGER)")
    con.commit()
    print("Students table created")
    con.close()

def program_4():
    con = connect()
    cur = con.cursor()
    cur.execute("PRAGMA table_info(students)")
    print(cur.fetchall())
    con.close()

def program_5():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print(cur.fetchall())
    con.close()

def program_6():
    con = connect()
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS students")
    con.commit()
    print("Students table deleted")
    con.close()

def program_7():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students'")
    print("Table exists" if cur.fetchone() else "Table not found")
    con.close()

def program_8():
    con = connect()
    cur = con.cursor()
    cur.execute("INSERT INTO students VALUES(1, 'Aman', 20, 85)")
    con.commit()
    print("One record inserted")
    con.close()

def program_9():
    con = connect()
    cur = con.cursor()
    data = [(2, "Riya", 21, 90), (3, "Rahul", 22, 75)]
    cur.executemany("INSERT INTO students VALUES(?, ?, ?, ?)", data)
    con.commit()
    print("Multiple records inserted")
    con.close()

def program_10():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    for row in cur.fetchall():
        print(row)
    con.close()

def program_11():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT name, marks FROM students")
    print(cur.fetchall())
    con.close()

def program_12():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM students WHERE marks > 80")
    print(cur.fetchall())
    con.close()

def program_13():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM students ORDER BY marks DESC")
    print(cur.fetchall())
    con.close()

def program_14():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM students")
    print("Total records:", cur.fetchone()[0])
    con.close()

def program_15():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 3")
    print(cur.fetchall())
    con.close()

def program_16():
    con = connect()
    cur = con.cursor()
    cur.execute("UPDATE students SET marks=95 WHERE id=1")
    con.commit()
    print("Marks updated")
    con.close()

def program_17():
    con = connect()
    cur = con.cursor()
    cur.execute("UPDATE students SET name='Karan' WHERE id=1")
    con.commit()
    print("Name updated")
    con.close()

def program_18():
    con = connect()
    cur = con.cursor()
    cur.execute("DELETE FROM students WHERE id=1")
    con.commit()
    print("Record deleted")
    con.close()

def program_19():
    con = connect()
    cur = con.cursor()
    cur.execute("DELETE FROM students WHERE marks < 40")
    con.commit()
    print("Students with marks below 40 deleted")
    con.close()

def program_20():
    con = connect()
    cur = con.cursor()
    cur.execute("DELETE FROM students")
    con.commit()
    print("Table is now empty")
    con.close()

def program_21():
    con = connect()
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS courses(id INTEGER, course TEXT)")
    cur.execute("INSERT INTO courses VALUES(1, 'MCA')")
    con.commit()
    print("Courses table created and course inserted")
    con.close()

def program_22():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM students INNER JOIN courses ON students.id=courses.id")
    print(cur.fetchall())
    con.close()

def program_23():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM students LEFT JOIN courses ON students.id=courses.id")
    print(cur.fetchall())
    con.close()

def program_24():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT AVG(marks) FROM students")
    print("Average marks:", cur.fetchone()[0])
    con.close()

def program_25():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT age, COUNT(*) FROM students GROUP BY age")
    print(cur.fetchall())
    con.close()

def program_26():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "Marks"])
        writer.writerows(cur.fetchall())
    print("Data exported to students.csv")
    con.close()

def program_27():
    con = connect()
    cur = con.cursor()
    try:
        with open("students.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                cur.execute("INSERT INTO students VALUES(?, ?, ?, ?)", row)
        con.commit()
        print("Data imported from students.csv")
    except FileNotFoundError:
        print("students.csv not found. Run Program 26 first.")
    con.close()

def program_28():
    con = None
    try:
        con = connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM students")
        print(cur.fetchall())
    except sqlite3.Error as error:
        print("Database error:", error)
    finally:
        if con:
            con.close()

def program_29():
    def insert_record():
        con = connect()
        cur = con.cursor()
        cur.execute("INSERT INTO students VALUES(4, 'Neha', 20, 88)")
        con.commit()
        con.close()
        print("Record inserted")

    def fetch_records():
        con = connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM students")
        print(cur.fetchall())
        con.close()

    insert_record()
    fetch_records()

def program_30():
    con = connect()
    cur = con.cursor()

    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = int(input("Enter ID: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = int(input("Enter marks: "))
        cur.execute("INSERT INTO students VALUES(?, ?, ?, ?)", (student_id, name, age, marks))
        con.commit()
        print("Student added")
    elif choice == "2":
        cur.execute("SELECT * FROM students")
        print(cur.fetchall())
    elif choice == "3":
        student_id = int(input("Enter student ID: "))
        marks = int(input("Enter new marks: "))
        cur.execute("UPDATE students SET marks=? WHERE id=?", (marks, student_id))
        con.commit()
        print("Marks updated")
    elif choice == "4":
        student_id = int(input("Enter student ID: "))
        cur.execute("DELETE FROM students WHERE id=?", (student_id,))
        con.commit()
        print("Student deleted")
    else:
        print("Invalid choice")

    con.close()

programs = {
    1: program_1, 2: program_2, 3: program_3, 4: program_4, 5: program_5,
    6: program_6, 7: program_7, 8: program_8, 9: program_9, 10: program_10,
    11: program_11, 12: program_12, 13: program_13, 14: program_14, 15: program_15,
    16: program_16, 17: program_17, 18: program_18, 19: program_19, 20: program_20,
    21: program_21, 22: program_22, 23: program_23, 24: program_24, 25: program_25,
    26: program_26, 27: program_27, 28: program_28, 29: program_29, 30: program_30
}

while True:
    print("\n========== LAB SHEET 08 ==========")
    print("Select a program (1-30)")
    print("0. Exit")

    try:
        choice = int(input("Enter program number: "))
        if choice == 0:
            print("Program ended")
            break
        elif choice in programs:
            programs[choice]()
        else:
            print("Please enter a number from 1 to 30")
    except Exception as error:
        print("Error:", error)
