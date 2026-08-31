from tkinter import *
import sqlite3
import random

# ---------------- DATABASE ---------------- #

conn = sqlite3.connect("flashcards.db")
cursor = conn.cursor()

try:
    with open("selected_category.txt", "r") as f:
        selected_category = f.read().strip()
except:
    selected_category = "Programming"

cursor.execute(
    "SELECT * FROM flashcards WHERE category=?",
    (selected_category,)
)

flashcards = cursor.fetchall()
random.shuffle(flashcards)

current_index = 0
correct_answers = 0
wrong_answers = 0
results = []

time_left = 30
timer_running = False



# ---------------- FUNCTIONS ---------------- #

def show_question():

    if len(flashcards) == 0:
        question_label.config(text="No Flashcards Found")
        counter_label.config(text="Flashcard 0 of 0")
        return

    question_label.config(
        text=flashcards[current_index][1]
    )

    answer_entry.delete(0, END)
    answer_entry.focus()

    counter_label.config(
        text=f"Question {current_index + 1} of {len(flashcards)}"
    )

    global time_left
    global timer_running

    time_left = 30

    timer_running = True

    timer_label.config(text="Time Left: 30s")

    update_timer()

def update_timer():

    global time_left
    global timer_running

    if not timer_running:
        return

    timer_label.config(
        text=f"Time Left: {time_left}s"
    )

    if time_left <= 0:
        timer_running = False
        auto_wrong()
        return

    time_left -= 1

    root.after(
    1000,
    update_timer
)


def auto_wrong():

    global current_index
    global wrong_answers
    global timer_running

    timer_running = False

    results.append(
        (
            flashcards[current_index][1],
            "No Answer",
            flashcards[current_index][2],
            "Wrong (Time Up)"
        )
    )

    wrong_answers += 1

    current_index += 1

    if current_index >= len(flashcards):
        show_result()
    else:
        show_question()


def submit_answer():
    global current_index
    global timer_running
    global correct_answers
    global wrong_answers

    timer_running = False


    if len(flashcards) == 0:
        return

    user_answer = answer_entry.get().strip().lower()

    correct_answer = (
        flashcards[current_index][2]
        .strip()
        .lower()
    )

    if user_answer == "":
        return

    if (
        user_answer in correct_answer
        or correct_answer in user_answer
    ):
        status = "Correct"
        correct_answers += 1
    else:
        status = "Wrong"
        wrong_answers += 1

    results.append(
        (
            flashcards[current_index][1],
            user_answer,
            flashcards[current_index][2],
            status
        )
    )

    current_index += 1

    if current_index >= len(flashcards):
        show_result()
    else:
        show_question()


def show_result():

    total = correct_answers + wrong_answers

    if total == 0:
        score = 0
    else:
        score = (
            correct_answers / total
        ) * 100

    # SAVE HISTORY

    conn2 = sqlite3.connect("quiz_history.db")
    cursor2 = conn2.cursor()

    cursor2.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        score INTEGER,
        correct_answers INTEGER,
        wrong_answers INTEGER
    )
    """)

    cursor2.execute(
        """
        INSERT INTO history(
        category,
        score,
        correct_answers,
        wrong_answers
        )
        VALUES(?,?,?,?)
        """,
        (
            selected_category,
            int(score),
            correct_answers,
            wrong_answers
        )
    )

    conn2.commit()
    conn2.close()

    # RESULT WINDOW

    result_window = Toplevel(root)
    result_window.title("Quiz Result")
    result_window.geometry("850x650")

    scrollbar = Scrollbar(result_window)
    scrollbar.pack(side=RIGHT, fill=Y)

    text_area = Text(
        result_window,
        font=("Segoe UI", 11),
        yscrollcommand=scrollbar.set
    )

    text_area.pack(
        fill=BOTH,
        expand=True
    )

    scrollbar.config(
        command=text_area.yview
    )

    text_area.insert(
        END,
        f"""
Category : {selected_category}

Total Questions : {total}

Correct Answers : {correct_answers}

Wrong Answers : {wrong_answers}

Score : {score:.0f}%

Performance :
{"Excellent" if score >= 90 else
"Very Good" if score >= 70 else
"Good" if score >= 50 else
"Needs Improvement"}

==================================================

"""
    )

    for q, user, correct, status in results:

        text_area.insert(
            END,
            f"""
Question:
{q}

Your Answer:
{user}

Correct Answer:
{correct}

Result:
{status}

--------------------------------------------------

"""
        )

    text_area.config(state=DISABLED)


# ---------------- WINDOW ---------------- #

root = Tk()
root.title("Flashcard Quiz")
root.geometry("900x600")
root.config(bg="#EAF4FF")

Label(
    root,
    text="FLASHCARD QUIZ",
    bg="#003366",
    fg="white",
    font=("Segoe UI", 22, "bold"),
    pady=10
).pack(fill=X)

# Category + Counter

info_frame = Frame(
    root,
    bg="#EAF4FF"
)
info_frame.pack(pady=10)

Label(
    info_frame,
    text=f"Category : {selected_category}",
    bg="#EAF4FF",
    font=("Segoe UI", 12, "bold")
).pack()

counter_label = Label(
    info_frame,
    text="",
    bg="#EAF4FF",
    font=("Segoe UI", 12)
)

counter_label.pack()



# Question Card

card_frame = Frame(
    root,
    bg="white",
    bd=3,
    relief=RIDGE
)

card_frame.place(
    relx=0.5,
    rely=0.45,
    anchor=CENTER,
    width=700,
    height=300
)

question_label = Label(
    card_frame,
    text="",
    bg="white",
    font=("Segoe UI", 16, "bold"),
    wraplength=600
)

question_label.pack(pady=30)

Label(
    card_frame,
    text="Your Answer",
    bg="white",
    font=("Segoe UI", 12, "bold")
).pack()

answer_entry = Entry(
    card_frame,
    width=50,
    font=("Segoe UI", 12)
)

answer_entry.pack(pady=15)
answer_entry.focus()

timer_label = Label(
    card_frame,
    text="Time Left: 30s",
    bg="white",
    fg="red",
    font=("Segoe UI", 12, "bold")
)

timer_label.pack(pady=5)


# Buttons

btn_frame = Frame(
    root,
    bg="#EAF4FF"
)

btn_frame.pack(
    side=BOTTOM,
    pady=40
)

Button(
    btn_frame,
    text="Submit Answer",
    command=submit_answer,
    bg="green",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    width=20
).grid(
    row=0,
    column=0,
    padx=20
)

show_question()

root.mainloop()

conn.close()
