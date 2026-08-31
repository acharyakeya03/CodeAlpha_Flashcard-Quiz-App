import sqlite3

conn = sqlite3.connect("flashcards.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM flashcards")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()