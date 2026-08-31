from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

# ---------------- DATABASE ---------------- #

conn = sqlite3.connect("flashcards.db")
cursor = conn.cursor()

# ---------------- FUNCTIONS ---------------- #

def load_data():

    tree.delete(*tree.get_children())

    cursor.execute("SELECT * FROM flashcards")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", END, values=row)


def search_data():

    keyword = search_entry.get()

    tree.delete(*tree.get_children())

    cursor.execute("""
    SELECT * FROM flashcards
    WHERE question LIKE ?
    OR category LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", END, values=row)


def delete_flashcard():

    selected = tree.focus()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Select a flashcard first"
        )
        return

    values = tree.item(selected, "values")

    flashcard_id = values[0]
    question = values[1]

    confirm = messagebox.askyesno(
        "Confirm Delete",
        f"Are you sure you want to delete this flashcard?\n\n{question}"
    )

    if not confirm:
        return

    cursor.execute(
        "DELETE FROM flashcards WHERE id=?",
        (flashcard_id,)
    )

    conn.commit()

    load_data()

    messagebox.showinfo(
        "Success",
        "Flashcard Deleted Successfully!"
    )


def refresh_data():

    search_entry.delete(0, END)
    load_data()

def edit_flashcard():

    selected = tree.focus()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a flashcard"
        )
        return

    values = tree.item(selected, "values")

    edit_window = Toplevel(root)
    edit_window.title("Edit Flashcard")
    edit_window.geometry("600x400")
    edit_window.config(bg="#EAF4FF")

    Label(
        edit_window,
        text="Question",
        bg="#EAF4FF",
        font=("Segoe UI", 11, "bold")
    ).pack(pady=10)

    question_entry = Entry(
        edit_window,
        width=50
    )

    question_entry.pack()
    question_entry.insert(0, values[1])

    Label(
        edit_window,
        text="Answer",
        bg="#EAF4FF",
        font=("Segoe UI", 11, "bold")
    ).pack(pady=10)

    answer_entry = Entry(
        edit_window,
        width=50
    )

    answer_entry.pack()
    answer_entry.insert(0, values[2])

    Label(
        edit_window,
        text="Category",
        bg="#EAF4FF",
        font=("Segoe UI", 11, "bold")
    ).pack(pady=10)

    category_combo = ttk.Combobox(
        edit_window,
        values=[
            "Programming",
            "Python",
            "DBMS",
            "Data Science",
            "General Knowledge"
        ],
        state="readonly"
    )

    category_combo.pack()
    category_combo.set(values[3])

    def save_changes():

        cursor.execute(
            """
            UPDATE flashcards
            SET question=?,
                answer=?,
                category=?
            WHERE id=?
            """,
            (
                question_entry.get(),
                answer_entry.get(),
                category_combo.get(),
                values[0]
            )
        )

        conn.commit()

        load_data()

        messagebox.showinfo(
            "Success",
            "Flashcard Updated"
        )

        edit_window.destroy()

    Button(
        edit_window,
        text="Save Changes",
        command=save_changes,
        bg="green",
        fg="white",
        width=20
    ).pack(pady=20)

# ---------------- WINDOW ---------------- #

root = Tk()
root.title("Manage Flashcards")
root.geometry("950x600")
root.config(bg="#EAF4FF")

# Header

Label(
    root,
    text="MANAGE FLASHCARDS",
    bg="#003366",
    fg="white",
    font=("Segoe UI", 20, "bold"),
    pady=10
).pack(fill=X)

# Search Frame

search_frame = Frame(root, bg="#EAF4FF")
search_frame.pack(pady=15)

Label(
    search_frame,
    text="Search:",
    bg="#EAF4FF",
    font=("Segoe UI", 11, "bold")
).grid(row=0, column=0)

search_entry = Entry(
    search_frame,
    width=30,
    font=("Segoe UI", 11)
)

search_entry.grid(row=0, column=1, padx=10)

Button(
    search_frame,
    text="Search",
    command=search_data,
    bg="#0A3D62",
    fg="white"
).grid(row=0, column=2, padx=5)

Button(
    search_frame,
    text="Refresh",
    command=refresh_data,
    bg="green",
    fg="white"
).grid(row=0, column=3, padx=5)

# Treeview

columns = (
    "ID",
    "Question",
    "Answer",
    "Category"
)

tree = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=18
)

for col in columns:
    tree.heading(col, text=col)

tree.column("ID", width=50)
tree.column("Question", width=300)
tree.column("Answer", width=300)
tree.column("Category", width=150)

tree.pack(pady=20)

# Buttons

btn_frame = Frame(root, bg="#EAF4FF")
btn_frame.pack()

Button(
    btn_frame,
    text="Edit Flashcard",
    command=edit_flashcard,
    bg="#0A3D62",
    fg="white",
    width=20
).grid(row=0, column=0, padx=10)

Button(
    btn_frame,
    text="Delete Flashcard",
    command=delete_flashcard,
    bg="red",
    fg="white",
    width=20
).grid(row=0, column=1, padx=10)

Button(
    btn_frame,
    text="Close",
    command=root.destroy,
    bg="gray",
    fg="white",
    width=20
).grid(row=0, column=2, padx=10)



load_data()

root.mainloop()

conn.close()