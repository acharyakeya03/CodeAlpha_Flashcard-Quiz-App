from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess

# ---------------- SIGNUP WINDOW ---------------- #

def open_signup():

    signup_window = Toplevel(root)
    signup_window.title("Create Account")
    signup_window.geometry("600x450")
    signup_window.config(bg="#EAF4FF")

    Label(
        signup_window,
        text="CREATE ACCOUNT",
        bg="#003366",
        fg="white",
        font=("Segoe UI", 18, "bold"),
        pady=10
    ).pack(fill=X)

    frame = Frame(signup_window, bg="#EAF4FF")
    frame.pack(pady=30)

    Label(
        frame,
        text="Username",
        bg="#EAF4FF",
        font=("Segoe UI", 12)
    ).grid(row=0, column=0, pady=10)

    signup_username = Entry(
        frame,
        width=30,
        font=("Segoe UI", 12)
    )
    signup_username.grid(row=0, column=1)

    Label(
        frame,
        text="Password",
        bg="#EAF4FF",
        font=("Segoe UI", 12)
    ).grid(row=1, column=0, pady=10)

    signup_password = Entry(
        frame,
        width=30,
        show="*",
        font=("Segoe UI", 12)
    )
    signup_password.grid(row=1, column=1)

    Label(
        frame,
        text="Confirm Password",
        bg="#EAF4FF",
        font=("Segoe UI", 12)
    ).grid(row=2, column=0, pady=10)

    confirm_password = Entry(
        frame,
        width=30,
        show="*",
        font=("Segoe UI", 12)
    )
    confirm_password.grid(row=2, column=1)

    def create_account():

        username = signup_username.get()
        password = signup_password.get()
        confirm = confirm_password.get()

        if username == "" or password == "" or confirm == "":
            messagebox.showerror(
                "Error",
                "All fields are required"
            )
            return

        if password != confirm:
            messagebox.showerror(
                "Error",
                "Passwords do not match"
            )
            return

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        try:

            cursor.execute("""
                INSERT INTO users(username,password)
                VALUES(?,?)
            """, (username, password))

            conn.commit()

            messagebox.showinfo(
                "Success",
                "Account Created Successfully"
            )

            signup_window.destroy()

        except sqlite3.IntegrityError:

            messagebox.showerror(
                "Error",
                "Username already exists"
            )

        conn.close()

    Button(
        signup_window,
        text="CREATE ACCOUNT",
        command=create_account,
        bg="green",
        fg="white",
        font=("Segoe UI", 12, "bold"),
        width=20
    ).pack(pady=20)

# ---------------- LOGIN FUNCTION ---------------- #

def login():

    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror(
            "Error",
            "All fields are required"
        )
        return

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE username=?
        AND password=?
        """,
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:

        messagebox.showinfo(
            "Success",
            "Login Successful"
        )

        root.destroy()

        subprocess.Popen(
            ["python", "dashboard.py"]
        )

    else:

        messagebox.showerror(
            "Error",
            "Invalid Username or Password"
        )

# ---------------- MAIN WINDOW ---------------- #

root = Tk()
root.title("Flashcard Quiz App - Login")
root.geometry("700x500")
root.config(bg="#EAF4FF")

Label(
    root,
    text="FLASHCARD QUIZ APP",
    bg="#003366",
    fg="white",
    font=("Segoe UI", 22, "bold"),
    pady=15
).pack(fill=X)

Label(
    root,
    text="LOGIN",
    bg="#EAF4FF",
    font=("Segoe UI", 18, "bold")
).pack(pady=30)

frame = Frame(root, bg="#EAF4FF")
frame.pack(pady=20)

Label(
    frame,
    text="Username",
    bg="#EAF4FF",
    font=("Segoe UI", 12)
).grid(row=0, column=0, pady=10)

username_entry = Entry(
    frame,
    width=30,
    font=("Segoe UI", 12)
)
username_entry.grid(row=0, column=1)

Label(
    frame,
    text="Password",
    bg="#EAF4FF",
    font=("Segoe UI", 12)
).grid(row=1, column=0, pady=10)

password_entry = Entry(
    frame,
    width=30,
    show="*",
    font=("Segoe UI", 12)
)
password_entry.grid(row=1, column=1)

Button(
    root,
    text="LOGIN",
    command=login,
    bg="#0A3D62",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    width=20
).pack(pady=10)

Button(
    root,
    text="CREATE ACCOUNT",
    command=open_signup,
    bg="green",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    width=20
).pack(pady=10)

Button(
    root,
    text="EXIT",
    command=root.destroy,
    bg="red",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    width=20
).pack(pady=10)

root.mainloop()