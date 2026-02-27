# 🧠 AI Grammar Checker

A full-stack AI-powered Grammar Checking Web Application built using **FastAPI (Backend)** and **HTML/CSS/JavaScript (Frontend)**.

This project allows users to register, login, and check grammar of text using the `language_tool_python` library.

---

## 🚀 Features

- 🔐 User Registration & Login
- 📝 Grammar Correction
- ❌ Highlighted Errors
- 💡 Suggestion List
- 📊 Grammar Score Calculation
- 🌙 Dark Mode UI
- 📡 REST API Architecture

---

## 🛠 Tech Stack

### 🔹 Backend
- Python
- FastAPI
- SQLAlchemy
- LanguageTool (language_tool_python)
- Uvicorn
- Pydantic

### 🔹 Frontend
- HTML
- CSS
- JavaScript (Fetch API)

---

## 📂 Project Structure

ai-grammar-checker/
│
├── frontend/
│   ├── login.html
│   ├── register.html
│   ├── grammar.html
│   ├── dashboard.html
│   ├── style.css
│   ├── script.js
│   └── Background.png
│
├── routers/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── .gitignore
└── README.md

---

## ⚙️ Backend Setup (Local)

### 1️⃣ Clone the repository

git clone https://github.com/SayaligShinde/ai-grammar-checker.git

### 2️⃣ Create virtual environment

python -m venv venv

### 3️⃣ Activate virtual environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 4️⃣ Install dependencies

pip install -r requirements.txt

### 5️⃣ Run FastAPI server

uvicorn main:app --reload

Backend runs at:
http://127.0.0.1:8000

Swagger documentation:
http://127.0.0.1:8000/docs

---

## 💻 Frontend Setup

Open:

frontend/login.html

Using:
- Live Server (VS Code recommended)
- Or directly in browser

---

## 📡 API Endpoints

### 🔹 POST /register

Registers new user

Request Body:
{
  "name": "string",
  "email": "string",
  "password": "string"
}

---

### 🔹 POST /login

Authenticates user

Request Body:
{
  "email": "string",
  "password": "string"
}

---

### 🔹 POST /check-grammar

Checks grammar and returns corrections

Request Body:
{
  "text": "Your sentence here"
}

Response:
{
  "corrected_text": "Corrected sentence",
  "total_errors": 2,
  "errors": [
    {
      "incorrect_text": "walk",
      "suggestions": ["walks"]
    }
  ]
}

---

## 🧠 How It Works

1. User enters text in frontend.
2. Frontend sends text to FastAPI backend using Fetch API.
3. Backend uses language_tool_python to detect grammar mistakes.
4. Errors and suggestions are returned as JSON.
5. Frontend highlights incorrect words and calculates grammar score.

---

## 🔐 Environment Variables (Recommended Practice)

Create a .env file:

SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///./users.db

Then load in Python:

from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

---

## 📌 Why This Project Is Valuable

This project demonstrates:

- REST API development
- Authentication system
- Database integration
- Async backend architecture
- Frontend-backend communication
- Real-world deployment readiness

---

## 🧪 Future Improvements

- JWT Authentication
- Role-based access
- Production database (PostgreSQL)
- Docker deployment
- Unit testing
- CI/CD pipeline

---

## 👩‍💻 Author

Sayali Shinde  
GitHub: https://github.com/SayaligShinde

---

⭐ If you like this project, give it a star!
