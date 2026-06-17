import sqlite3

conn = sqlite3.connect("internship.db")

cursor = conn.cursor()

# Students Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    department TEXT,
    attendance INTEGER DEFAULT 0,
    tasks_completed INTEGER DEFAULT 0,
    rating INTEGER DEFAULT 0
)
""")

# Tasks Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT,
    task_title TEXT,
    task_description TEXT,
    status TEXT
)
""")

# Mentor Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")