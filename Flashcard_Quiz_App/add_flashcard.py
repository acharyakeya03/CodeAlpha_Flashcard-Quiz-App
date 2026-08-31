from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

# ---------------- DATABASE ---------------- #

conn = sqlite3.connect("flashcards.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS flashcards(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    category TEXT NOT NULL
)
""")

conn.commit()

# ---------------- FUNCTIONS ---------------- #

def save_flashcard():

    question = question_entry.get().strip()
    answer = answer_entry.get().strip()
    category = category_combo.get().strip()

    if question == "":
        messagebox.showerror("Error", "Please enter a question")
        return

    if answer == "":
        messagebox.showerror("Error", "Please enter an answer")
        return

    cursor.execute(
        "INSERT INTO flashcards(question, answer, category) VALUES (?, ?, ?)",
        (question, answer, category)
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Flashcard saved successfully!"
    )

    question_entry.delete(0, END)
    answer_entry.delete(0, END)
    category_combo.set("Programming")

    question_entry.focus()


def clear_fields():
    question_entry.delete(0, END)
    answer_entry.delete(0, END)
    category_combo.set("Programming")


def close_app():
    conn.close()
    root.destroy()

# ---------------- WINDOW ---------------- #

root = Tk()
root.title("Flashcard Quiz App - Add Flashcard")
root.geometry("800x500")
root.config(bg="#EAF4FF")
root.resizable(False, False)

# ---------------- HEADER ---------------- #

header = Label(
    root,
    text="ADD FLASHCARD",
    bg="#003366",
    fg="white",
    font=("Segoe UI", 22, "bold"),
    pady=15
)
header.pack(fill=X)

# ---------------- FRAME ---------------- #

frame = Frame(
    root,
    bg="white",
    bd=2,
    relief=RIDGE
)

frame.place(
    relx=0.5,
    rely=0.5,
    anchor=CENTER,
    width=650,
    height=300
)

# ---------------- QUESTION ---------------- #

Label(
    frame,
    text="Question",
    bg="white",
    font=("Segoe UI", 12, "bold")
).place(x=40, y=40)

question_entry = Entry(
    frame,
    width=45,
    font=("Segoe UI", 12)
)

question_entry.place(x=180, y=40)

# ---------------- ANSWER ---------------- #

Label(
    frame,
    text="Answer",
    bg="white",
    font=("Segoe UI", 12, "bold")
).place(x=40, y=100)

answer_entry = Entry(
    frame,
    width=45,
    font=("Segoe UI", 12)
)

answer_entry.place(x=180, y=100)

# ---------------- CATEGORY ---------------- #

Label(
    frame,
    text="Category",
    bg="white",
    font=("Segoe UI", 12, "bold")
).place(x=40, y=160)

category_combo = ttk.Combobox(
    frame,
    state="readonly",
    width=42,
    values=[
        "Programming",
        "Python",
        "DBMS",
        "Data Science",
        "General Knowledge"
    ]
)

category_combo.place(x=180, y=160)
category_combo.set("Programming")

# ---------------- BUTTONS ---------------- #

Button(
    frame,
    text="SAVE",
    command=save_flashcard,
    bg="#0A3D62",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=12
).place(x=100, y=230)

Button(
    frame,
    text="CLEAR",
    command=clear_fields,
    bg="gray",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=12
).place(x=260, y=230)

Button(
    frame,
    text="CLOSE",
    command=close_app,
    bg="red",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=12
).place(x=420, y=230)

root.mainloop()