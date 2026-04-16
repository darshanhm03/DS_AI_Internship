import sqlite3
import pandas as pd


conn = sqlite3.connect("internship.db")
cursor = conn.cursor()


cursor.execute("DROP TABLE IF EXISTS interns")


cursor.execute("""
CREATE TABLE interns (
    intern_id INTEGER PRIMARY KEY,
    intern_name TEXT,
    track TEXT,
    stipend INTEGER
)
""")


intern_data = [
    ('Rahul', 'Data Science', 8000),
    ('Anita', 'AI/ML', 6000),
    ('Vikram', 'Cyber Security', 4000),
    ('Neha', 'Data Science', 5000),
    ('Arjun', 'AI/ML', 7000)
]

cursor.executemany("""
INSERT INTO interns (intern_name, track, stipend)
VALUES (?, ?, ?)
""", intern_data)

conn.commit()


filter_query = """
SELECT *
FROM interns
WHERE track = 'Data Science'
AND stipend > 5000
"""

df_filter = pd.read_sql_query(filter_query, conn)
print("\nFiltered Data (Data Science & stipend > 5000):")
print(df_filter)


avg_query = """
SELECT track,
       AVG(stipend) AS average_stipend
FROM interns
GROUP BY track
"""

df_avg = pd.read_sql_query(avg_query, conn)
print("\nAverage Stipend Per Track:")
print(df_avg)


count_query = """
SELECT track,
       COUNT(*) AS total_interns
FROM interns
GROUP BY track
"""

df_count = pd.read_sql_query(count_query, conn)
print("\nNumber of Interns Per Track:")
print(df_count)


conn.close()