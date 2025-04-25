from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.database import SessionLocal
from app.services import auth_service


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.get("/ping")
async def ping():
    return {"message": "Auth router is working!"}


# Dependency برای گرفتن session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", response_model=schemas.UserResponse)
def register(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    user = auth_service.register_user(
        db,
        username=user_data.username,
        email=user_data.email,
        password=user_data.password
    )
    return user


@router.post("/login")
def login(user_data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = auth_service.authenticate_user(db, user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    token = auth_service.generate_token(user)
    return {"access_token": token, "token_type": "bearer"}