from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.base import get_db
from src.db.schema import User, UserCreate

from src.func.create_user import create_user as create_user_func
from src.func.get_user import get_user as get_user_func

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    result = create_user_func(user.username, user.email, db)
    if not result:
        raise HTTPException(status_code=400, detail="User with this username or email already exists.")
    return result

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_func(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
