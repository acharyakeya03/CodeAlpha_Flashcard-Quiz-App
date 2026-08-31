from tkinter import *
from tkinter import ttk
import subprocess

def start_quiz():
    selected_category = category_combo.get()

    with open("selected_category.txt", "w") as f:
        f.write(selected_category)

    subprocess.Popen(["python", "quiz.py"])


root = Tk()
root.title("Select Quiz Category")
root.geometry("500x300")
root.config(bg="#EAF4FF")

Label(
    root,
    text="SELECT CATEGORY",
    font=("Segoe UI", 18, "bold"),
    bg="#003366",
    fg="white",
    pady=10
).pack(fill=X)

Label(
    root,
    text="Choose a category:",
    font=("Segoe UI", 12),
    bg="#EAF4FF"
).pack(pady=30)

category_combo = ttk.Combobox(
    root,
    state="readonly",
    values=[
        "Programming",
        "Python",
        "DBMS",
        "Data Science",
        "General Knowledge"
    ],
    width=30
)

category_combo.pack()
category_combo.set("Programming")

Button(
    root,
    text="START QUIZ",
    command=start_quiz,
    bg="#0A3D62",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    width=15
).pack(pady=30)

root.mainloop()