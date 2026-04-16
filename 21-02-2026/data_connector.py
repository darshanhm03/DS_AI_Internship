import sqlite3
import pandas as pd

conn = sqlite3.connect("internship.db")
cursor = conn.cursor()


cursor.execute("DROP TABLE IF EXISTS interns")
cursor.execute("DROP TABLE IF EXISTS mentors")


cursor.execute("""
CREATE TABLE interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")


cursor.execute("""
CREATE TABLE mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT,
    track TEXT
)
""")


cursor.executemany("""
INSERT INTO interns (name, track, stipend)
VALUES (?, ?, ?)
""", [
    ("Aisha", "Data Science", 15000),
    ("Rahul", "Web Dev", 12000),
    ("Meera", "Data Science", 16000),
    ("Arjun", "Cyber Security", 14000),
    ("Priya", "Web Dev", 13000)
])


cursor.executemany("""
INSERT INTO mentors (mentor_name, track)
VALUES (?, ?)
""", [
    ("Dr. Sharma", "Data Science"),
    ("Mr. Verma", "Web Dev"),
    ("Ms. Iyer", "Cyber Security")
])

conn.commit()


query = """
SELECT 
    interns.name AS Intern_Name,
    interns.track AS Track,
    mentors.mentor_name AS Mentor
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track
"""

df = pd.read_sql_query(query, conn)

print("\nJoined Data:")
print(df)

conn.close()