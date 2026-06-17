import sqlite3

conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# View Students
print("\n--- STUDENTS ---")
for row in cursor.execute("SELECT * FROM students"):
    print(row)

# View Tasks
print("\n--- TASKS ---")
for row in cursor.execute("SELECT * FROM tasks"):
    print(row)

conn.close()