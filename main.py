"""
#Start
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "AI Grammar Checker Backend Running"}
"""

"""
#database.py
from fastapi import FastAPI
from database import engine

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Database Conneceted Successfully"}
"""
"""
#models.py
from fastapi import FastAPI
from database import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "User table created successfully"}


from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal
import bcrypt

#------------REGISTER---------------
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

@app.post("/register")
def register(user: UserCreate):
    db: Session = SessionLocal()

    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

    new_user = models.User(
        name=user.name,
        email=user.email,
        password=hashed_password.decode('utf-8')
    )

    db.add(new_user)
    db.commit()
    db.close()

    return {"message": "User registered successfully"}

#--------------LOGIN------------------
from fastapi import HTTPException

class UserLogin(BaseModel):
    email: str
    password: str


@app.post("/login")
def login(user: UserLogin):
    db: Session = SessionLocal()

    existing_user = db.query(models.User).filter(models.User.email == user.email).first()

    if not existing_user:
        db.close()
        raise HTTPException(status_code=400, detail="User not found")

    if not bcrypt.checkpw(user.password.encode('utf-8'), existing_user.password.encode('utf-8')):
        db.close()
        raise HTTPException(status_code=400, detail="Incorrect password")

    db.close()

    return {"message": "Login successful"}

#-----------CHECK-GRAMMAR--------------
import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

class TextInput(BaseModel):
    text: str


@app.post("/check-grammar")
def check_grammar(data: TextInput):
    matches = tool.check(data.text)
    corrected_text = language_tool_python.utils.correct(data.text, matches)

    errors = []

    for match in matches:
        errors.append({
            "message": match.message,
            "incorrect_text": data.text[match.offset: match.offset + match.error_length],
            "suggestions": match.replacements
        })

    return {
        "original_text": data.text,
        "corrected_text": corrected_text,
        "total_errors": len(errors),
        "errors": errors
    }
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from routers import auth, grammar

app = FastAPI()

# CORS must come AFTER app is created
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(grammar.router)

@app.get("/")
def home():
    return {"message": "AI Grammar Checker API Running"}

