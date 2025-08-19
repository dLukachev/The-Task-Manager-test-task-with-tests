from pydantic import BaseModel
from sqlalchemy import UUID

class User(BaseModel):
    id: UUID
    username: str
    email: str

class UserCreate(BaseModel):
    username: str
    email: str

class Task(BaseModel):
    id: UUID
    title: str
    description: str
    status: str
    user_id: int

class TaskCreate(BaseModel):
    title: str
    description: str
    status: str = "pending"
    user_id: int