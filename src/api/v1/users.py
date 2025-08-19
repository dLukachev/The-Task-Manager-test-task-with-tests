from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.base import get_db
from src.db.schema import User, UserCreate

from func.create_user import create_user as create_user_func

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    result = create_user_func(user.username, user.email, db)
    return result

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
