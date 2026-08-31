import sqlite3

conn = sqlite3.connect("flashcards.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS flashcards(
id INTEGER PRIMARY KEY AUTOINCREMENT,
question TEXT,
answer TEXT
)
""")

conn.commit()
conn.close()