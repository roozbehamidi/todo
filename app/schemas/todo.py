from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# ⬅️ اسکیمای ایجاد ToDo
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None

# ⬅️ اسکیمای پاسخ ToDo
class TodoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    created_at: datetime
    updated_at: datetime    

    model_config = {
        "from_attributes": True
    }


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None