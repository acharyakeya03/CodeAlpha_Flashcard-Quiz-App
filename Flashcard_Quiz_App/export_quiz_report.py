from reportlab.pdfgen import canvas
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("quiz_history.db")
cursor = conn.cursor()

cursor.execute("""
SELECT *
FROM history
ORDER BY id DESC
LIMIT 1
""")

record = cursor.fetchone()

conn.close()

if record:

    pdf = canvas.Canvas("Quiz_Report.pdf")

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(150, 800, "FLASHCARD QUIZ REPORT")

    pdf.setFont("Helvetica", 12)

    pdf.drawString(100, 730, f"Category : {record[1]}")
    pdf.drawString(100, 700, f"Score : {record[2]}%")
    pdf.drawString(100, 670, f"Correct Answers : {record[3]}")
    pdf.drawString(100, 640, f"Wrong Answers : {record[4]}")

    pdf.save()

    messagebox.showinfo(
        "Success",
        "Quiz_Report.pdf Generated Successfully"
    )

else:

    messagebox.showerror(
        "Error",
        "No Quiz History Found"
    )