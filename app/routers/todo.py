from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas
from app.utils import get_current_user
from app.models.user import User
from typing import Optional
from fastapi import Query
from app.services import todo_service

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)

# Dependency برای session دیتابیس
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📌 مسیر: ایجاد یک کار جدید برای کاربر لاگین‌شده
@router.post("/", response_model=schemas.TodoResponse)
def create_todo(
    todo_data: schemas.TodoCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    user = db.query(User).filter(User.email == current_user).first()
    return todo_service.create_todo(db, user, todo_data.title, todo_data.description)




@router.get("/", response_model=list[schemas.TodoResponse])
def get_my_todos(
    completed: Optional[bool] = Query(None, description="Filter by completion status"),
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    user = db.query(User).filter(User.email == current_user).first()
    return todo_service.get_all_todos(db, user, completed=completed)




@router.get("/{todo_id}", response_model=schemas.TodoResponse)
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    user = db.query(User).filter(User.email == current_user).first()
    return todo_service.get_todo_by_id(db, user, todo_id)



@router.put("/{todo_id}", response_model=schemas.TodoResponse)
def update_todo(
    todo_id: int,
    todo_data: schemas.TodoUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    user = db.query(User).filter(User.email == current_user).first()
    updates = todo_data.dict(exclude_unset=True)
    return todo_service.update_todo(db, user, todo_id, updates)


@router.delete("/{todo_id}")
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    user = db.query(User).filter(User.email == current_user).first()
    return todo_service.delete_todo(db, user, todo_id)

