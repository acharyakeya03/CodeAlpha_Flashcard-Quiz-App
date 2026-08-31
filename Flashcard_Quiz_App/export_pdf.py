from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import sqlite3
from tkinter import messagebox

# Database Connection
conn = sqlite3.connect("flashcards.db")
cursor = conn.cursor()

cursor.execute("""
SELECT question, answer, category
FROM flashcards
ORDER BY category
""")

records = cursor.fetchall()

pdf = SimpleDocTemplate("Flashcards_Report.pdf")

styles = getSampleStyleSheet()

content = []

title = Paragraph("Flashcard Quiz App Report", styles['Title'])
content.append(title)
content.append(Spacer(1, 20))

for question, answer, category in records:

    content.append(
        Paragraph(
            f"<b>Category:</b> {category}",
            styles['Heading3']
        )
    )

    content.append(
        Paragraph(
            f"<b>Question:</b> {question}",
            styles['BodyText']
        )
    )

    content.append(
        Paragraph(
            f"<b>Answer:</b> {answer}",
            styles['BodyText']
        )
    )

    content.append(Spacer(1, 10))

pdf.build(content)

messagebox.showinfo(
    "Success",
    "PDF Report Generated Successfully"
)

conn.close()