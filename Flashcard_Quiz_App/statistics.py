from tkinter import *
import sqlite3

conn = sqlite3.connect("flashcards.db")
cursor = conn.cursor()

root = Tk()
root.title("Quiz Statistics")
root.geometry("500x500")
root.config(bg="#EAF4FF")

Label(
    root,
    text="QUIZ STATISTICS",
    bg="#003366",
    fg="white",
    font=("Segoe UI", 18, "bold"),
    pady=10
).pack(fill=X)

cursor.execute("SELECT COUNT(*) FROM flashcards")
total = cursor.fetchone()[0]

Label(
    root,
    text=f"Total Flashcards : {total}",
    font=("Segoe UI", 14, "bold"),
    bg="#EAF4FF"
).pack(pady=20)

categories = [
    "Programming",
    "Python",
    "DBMS",
    "Data Science",
    "General Knowledge"
]

for category in categories:

    cursor.execute(
        "SELECT COUNT(*) FROM flashcards WHERE category=?",
        (category,)
    )

    count = cursor.fetchone()[0]

    Label(
        root,
        text=f"{category} : {count}",
        font=("Segoe UI", 12),
        bg="#EAF4FF"
    ).pack(pady=5)

Button(
    root,
    text="Close",
    command=root.destroy,
    bg="red",
    fg="white",
    width=15
).pack(pady=20)

root.mainloop()

conn.close()