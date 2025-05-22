from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.todo import Todo
from app.models.user import User
from typing import Optional


def create_todo(db: Session, user: User, title: str, description: str = None):
    todo = Todo(title=title, description=description, user_id=user.id)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def get_all_todos(db: Session, user: User, completed: Optional[bool] = None):
    query = db.query(Todo).filter(Todo.user_id == user.id)
    
    if completed is not None:
        query = query.filter(Todo.completed == completed)
    
    return query.all()


def get_todo_by_id(db: Session, user: User, todo_id: int):
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return todo

def update_todo(db: Session, user: User, todo_id: int, updates: dict):
    todo = get_todo_by_id(db, user, todo_id)
    for key, value in updates.items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(db: Session, user: User, todo_id: int):
    todo = get_todo_by_id(db, user, todo_id)
    db.delete(todo)
    db.commit()
    return {"message": f"ToDo {todo_id} deleted successfully"}
