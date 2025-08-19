from pydantic import BaseModel, ConfigDict
from uuid import UUID

class User(BaseModel):
    id: int
    username: str
    email: str

class UserCreate(BaseModel):
    username: str
    email: str

class Task(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: UUID
    title: str
    description: str
    status: str 
    user_id: int

class TaskCreate(BaseModel):
    title: str
    description: str
    status: str = "create"
    user_id: int