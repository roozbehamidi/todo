from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.utils import verify_password, create_access_token, hash_password

# ثبت‌نام کاربر جدید
def register_user(db: Session, username: str, email: str, password: str):
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pwd = hash_password(password)
    new_user = User(username=username, email=email, hashed_password=hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# احراز هویت کاربر
def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

# صدور توکن
def generate_token(user: User):
    return create_access_token({"sub": user.email})
