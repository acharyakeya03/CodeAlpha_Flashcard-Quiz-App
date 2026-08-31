import sqlite3

conn = sqlite3.connect("quiz_history.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    score INTEGER,
    correct_answers INTEGER,
    wrong_answers INTEGER
)
""")

conn.commit()
conn.close()

print("History Database Created Successfully")