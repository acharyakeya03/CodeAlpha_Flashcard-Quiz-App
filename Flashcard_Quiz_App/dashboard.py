from tkinter import *
import subprocess
import sqlite3

# ---------------- FUNCTIONS ---------------- #

def logout():
    root.destroy()

    subprocess.Popen(
        ["python", "login.py"]
    )


def open_add_flashcard():
    subprocess.Popen(
        ["python", "add_flashcard.py"]
    )


def open_quiz():
    subprocess.Popen(
        ["python", "category_quiz.py"]
    )


def open_manage():
    subprocess.Popen(
        ["python", "manage_flashcards.py"]
    )


def open_statistics():
    subprocess.Popen(
        ["python", "statistics.py"]
    )


def open_history():
    subprocess.Popen(
        ["python", "history.py"]
    )


def open_export():
    subprocess.Popen(
        ["python", "export_quiz_report.py"]
    )


# ---------------- DATABASE ---------------- #

conn = sqlite3.connect("flashcards.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM flashcards")
total_flashcards = cursor.fetchone()[0]

conn.close()


# ---------------- WINDOW ---------------- #

root = Tk()
root.title("Flashcard Quiz App - Dashboard")
root.geometry("950x700")
root.config(bg="#EAF4FF")
root.resizable(False, False)


# ---------------- HEADER ---------------- #

header = Frame(
    root,
    bg="#003366",
    height=100
)

header.pack(fill=X)

Label(
    header,
    text="FLASHCARD QUIZ APP",
    bg="#003366",
    fg="white",
    font=("Segoe UI", 26, "bold")
).pack(pady=(15, 2))

Label(
    header,
    text="Learn • Practice • Improve",
    bg="#003366",
    fg="white",
    font=("Segoe UI", 11)
).pack()


# ---------------- WELCOME ---------------- #

Label(
    root,
    text="Welcome to Flashcard Quiz App!",
    bg="#EAF4FF",
    fg="#003366",
    font=("Segoe UI", 20, "bold")
).pack(pady=(25, 5))


Label(
    root,
    text="Manage your flashcards and test your knowledge",
    bg="#EAF4FF",
    fg="gray",
    font=("Segoe UI", 11)
).pack()


# ---------------- FLASHCARD COUNT ---------------- #

count_frame = Frame(
    root,
    bg="white",
    bd=2,
    relief=RIDGE
)

count_frame.pack(
    pady=20,
    ipadx=35,
    ipady=8
)

Label(
    count_frame,
    text="TOTAL FLASHCARDS",
    bg="white",
    fg="#003366",
    font=("Segoe UI", 10, "bold")
).pack()

Label(
    count_frame,
    text=str(total_flashcards),
    bg="white",
    fg="#0A3D62",
    font=("Segoe UI", 22, "bold")
).pack()


# ---------------- BUTTONS FRAME ---------------- #

btn_frame = Frame(
    root,
    bg="#EAF4FF"
)

btn_frame.pack(pady=10)


# ---------------- BUTTON STYLE ---------------- #

button_font = (
    "Segoe UI",
    11,
    "bold"
)


# ---------------- ADD FLASHCARD ---------------- #

Button(
    btn_frame,
    text="ADD FLASHCARD",
    width=22,
    height=2,
    bg="#0A3D62",
    fg="white",
    font=button_font,
    command=open_add_flashcard
).grid(
    row=0,
    column=0,
    padx=15,
    pady=10
)


# ---------------- START QUIZ ---------------- #

Button(
    btn_frame,
    text="START QUIZ",
    width=22,
    height=2,
    bg="#0A3D62",
    fg="white",
    font=button_font,
    command=open_quiz
).grid(
    row=0,
    column=1,
    padx=15,
    pady=10
)


# ---------------- MANAGE FLASHCARDS ---------------- #

Button(
    btn_frame,
    text="MANAGE FLASHCARDS",
    width=22,
    height=2,
    bg="#0A3D62",
    fg="white",
    font=button_font,
    command=open_manage
).grid(
    row=1,
    column=0,
    padx=15,
    pady=10
)


# ---------------- QUIZ STATISTICS ---------------- #

Button(
    btn_frame,
    text="QUIZ STATISTICS",
    width=22,
    height=2,
    bg="#0A3D62",
    fg="white",
    font=button_font,
    command=open_statistics
).grid(
    row=1,
    column=1,
    padx=15,
    pady=10
)


# ---------------- QUIZ HISTORY ---------------- #

Button(
    btn_frame,
    text="QUIZ HISTORY",
    width=22,
    height=2,
    bg="#0A3D62",
    fg="white",
    font=button_font,
    command=open_history
).grid(
    row=2,
    column=0,
    padx=15,
    pady=10
)


# ---------------- EXPORT PDF ---------------- #

Button(
    btn_frame,
    text="EXPORT PDF",
    width=22,
    height=2,
    bg="#0A3D62",
    fg="white",
    font=button_font,
    command=open_export
).grid(
    row=2,
    column=1,
    padx=15,
    pady=10
)


# ---------------- LOGOUT ---------------- #

Button(
    root,
    text="LOGOUT",
    width=22,
    height=2,
    bg="orange",
    fg="white",
    font=button_font,
    command=logout
).pack(pady=20)


# ---------------- FOOTER ---------------- #

Label(
    root,
    text="Flashcard Quiz App • Keep Learning!",
    bg="#EAF4FF",
    fg="gray",
    font=("Segoe UI", 9)
).pack(
    side=BOTTOM,
    pady=8
)


root.mainloop()