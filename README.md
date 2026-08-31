# 🧠 Flashcard Quiz App

A desktop-based **Flashcard Quiz Application** developed using **Python, Tkinter, and SQLite**. The application allows users to create, manage, and practice flashcards through category-based quizzes with a timer, automatic evaluation, quiz statistics, and quiz history.

---

## 📌 Project Overview

The Flashcard Quiz App is designed as an interactive learning application that helps users improve their knowledge through flashcard-based quizzes.

Users can create an account, add and manage flashcards, select a category, attempt quizzes, enter their own answers, and receive detailed results after completing the quiz.

The application also includes a **30-second timer for each question**. If the user does not answer within the given time, the question is automatically marked as wrong.

---

## ✨ Features

### 🔐 Login & Signup
- User registration with username and password
- Secure login validation
- Username uniqueness checking
- Separate Create Account window
- Logout functionality

### 📝 Flashcard Management
- Add new flashcards
- Store questions and answers
- Organize flashcards by category
- Search and manage existing flashcards
- Edit/update flashcards
- Delete unwanted flashcards

### 📚 Quiz System
- Category-based quizzes
- Randomized flashcard questions
- User enters the answer manually
- Submit Answer functionality
- Automatic answer evaluation
- Correct and wrong answer tracking
- Detailed result after completing the quiz

### ⏱️ Timer
- 30-second timer for every question
- Timer resets for each new question
- Automatically marks unanswered questions as wrong when time expires
- Displays remaining time to the user

### 📊 Quiz Results
After completing a quiz, the application displays:
- Selected category
- Total questions
- Correct answers
- Wrong answers
- Overall score
- Performance level
- User's answer
- Correct answer
- Result for each question

### 📈 Quiz Statistics
- View quiz performance
- Track quiz scores
- Category-based statistics
- Monitor learning progress

### 📜 Quiz History
- Stores completed quiz attempts
- Saves category
- Saves score
- Saves correct answers
- Saves wrong answers
- Allows users to review previous quiz performance

### 📄 PDF Report
- Export quiz information as a PDF report
- Useful for maintaining a record of quiz performance

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Main programming language |
| **Tkinter** | Graphical User Interface |
| **SQLite** | Database management |
| **Random** | Randomizing quiz questions |
| **Subprocess** | Opening different application modules |
| **ReportLab** | PDF report generation |

---

## 🗂️ Project Structure

```text
Flashcard_Quiz_App/
│
├── main.py
├── login.py
├── add_flashcard.py
├── category_quiz.py
├── quiz.py
├── manage_flashcards.py
├── statistics.py
├── history.py
├── export_quiz_report.py
│
├── flashcards.db
├── users.db
├── quiz_history.db
├── selected_category.txt
│
└── README.md

📂 Database Details
flashcards.db

Stores flashcard information such as:

ID
Question
Answer
Category
users.db

Stores registered user information:

ID
Username
Password
quiz_history.db

Stores completed quiz results:

ID
Category
Score
Correct Answers
Wrong Answers
🎯 Available Categories

The application supports categories such as:

Programming
Python
DBMS
Data Science
General Knowledge
🚀 How to Run the Project
Step 1: Install Python

Make sure Python is installed on your computer.

Check the installation using:

python --version
Step 2: Download or Clone the Repository

Clone the project using:

git clone YOUR_GITHUB_REPOSITORY_URL

Then open the project folder.

Step 3: Install Required Library

For PDF generation, install ReportLab:

pip install reportlab

Tkinter and SQLite are generally included with standard Python installations.

Step 4: Run the Application

Start the application using:

python main.py

The application will open the Login / Signup screen.

🔄 Application Workflow
        START
          │
          ▼
   Login / Signup
          │
          ▼
       Dashboard
          │
    ┌─────┼──────────────┐
    │     │              │
    ▼     ▼              ▼
  Add   Start Quiz   Manage Flashcards
          │
          ▼
    Select Category
          │
          ▼
    Start Questions
          │
          ▼
   Enter Your Answer
          │
          ▼
      Submit
          │
          ▼
  Evaluate Answer
          │
          ▼
     Next Question
          │
          ▼
    Quiz Completed
          │
          ▼
     Show Results
          │
     ┌────┴─────┐
     ▼          ▼
   History   Statistics
⏱️ Quiz Timer Workflow

Each question has a 30-second time limit.

Question Appears
       │
       ▼
   Timer = 30s
       │
       ▼
 User enters answer
       │
       ├───────────────┐
       │               │
       ▼               ▼
    Submit          Time = 0
       │               │
       ▼               ▼
 Evaluate Answer   Mark as Wrong
       │               │
       └───────┬───────┘
               ▼
        Next Question
📊 Answer Evaluation

The application compares the user's entered answer with the stored correct answer.

If the answer matches:

Correct Answer ✅

Otherwise:

Wrong Answer ❌

If the timer reaches zero before an answer is submitted:

Wrong (Time Up) ⏱️
🎨 User Interface

The application uses a simple and consistent desktop interface designed with Tkinter.

Main UI Theme
Light blue background
Dark blue headers
Green action buttons
Red warning/error buttons
Segoe UI fonts
Clean card-based quiz layout
📈 Scoring System

The score is calculated using:

Score = (Correct Answers / Total Questions) × 100
Performance Levels
Score	Performance
90% – 100%	Excellent
70% – 89%	Very Good
50% – 69%	Good
Below 50%	Needs Improvement
💡 Learning Outcomes

Through this project, I gained practical experience in:

Python programming
Object-oriented and modular programming concepts
Tkinter GUI development
SQLite database integration
CRUD operations
User authentication
File handling
Event-driven programming
Timer implementation
Quiz evaluation logic
Data management
PDF report generation
Debugging and error handling
Building a complete desktop application
🔮 Future Improvements

Possible future enhancements include:

Password hashing and stronger authentication
User profile management
Difficulty levels
Leaderboard system
More advanced analytics
Graphical performance charts
Dark mode
Sound effects
Multiple-choice questions
Cloud database integration
Online multiplayer quiz mode
👩‍💻 Developer

Keya Acharya

BCA – Data Science

Interested in:

Python
Data Science
Full Stack Development
Software Development
🏆 Internship Project

This project was developed as part of my Python Full Stack Development learning experience with CodeAlpha.

The project helped me apply programming and database concepts to a practical desktop application.

📜 License

This project is created for educational and learning purposes.

You are welcome to explore the code and use it as a reference for learning.


### One important thing before uploading to GitHub

Since your project contains `users.db`, **don't upload a database containing real passwords or personal user data**. For a student project, it's better to either upload an empty/sample database or add the database files to `.gitignore`.

You can also add a `.gitignore` like this:

```gitignore
__pycache__/
*.pyc

users.db
quiz_history.db

selected_category.txt

You can keep flashcards.db only if it contains sample/non-personal flashcards
