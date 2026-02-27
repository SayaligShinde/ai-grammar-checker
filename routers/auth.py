from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models
import bcrypt
from schemas import UserCreate, UserLogin

router = APIRouter()

@router.post("/register")
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


@router.post("/login")
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
