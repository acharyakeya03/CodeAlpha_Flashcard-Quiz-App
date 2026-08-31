from tkinter import *
import sqlite3

root = Tk()
root.title("Quiz History")
root.geometry("800x500")
root.config(bg="#EAF4FF")

Label(
    root,
    text="QUIZ HISTORY",
    bg="#003366",
    fg="white",
    font=("Segoe UI", 20, "bold"),
    pady=10
).pack(fill=X)

text_area = Text(
    root,
    font=("Consolas", 11)
)

text_area.pack(
    fill=BOTH,
    expand=True,
    padx=20,
    pady=20
)

conn = sqlite3.connect("quiz_history.db")

cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM history"
)

records = cursor.fetchall()

for row in records:

    text_area.insert(
        END,
        f"""
Category : {row[1]}

Score : {row[2]}%

Correct : {row[3]}

Wrong : {row[4]}

-----------------------------
"""
    )

conn.close()

root.mainloop()