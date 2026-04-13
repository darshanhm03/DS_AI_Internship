import sqlite3

conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

cursor.execute("""
INSERT INTO interns (name, track, stipend) VALUES
('Alice', 'Data Science', 15000),
('Rahul', 'Web Dev', 12000),
('Neha', 'Data Science', 18000),
('Arjun', 'UI/UX', 10000),
('Priya', 'Web Dev', 14000)
""")

conn.commit()

cursor.execute("SELECT name, track FROM interns")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()