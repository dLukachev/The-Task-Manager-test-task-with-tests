from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.base import get_db
from src.db.schema import User, UserCreate

from src.func.create_user import create_user as create_user_func
from src.func.get_user import get_user as get_user_func
from src.func.edit_user import edit_user as edit_user_func
from src.func.delete_user import delete_user as delete_user_func

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

@router.put("/users/{user_id}", response_model=User)
def edit_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_func(user_id, db)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    updated_user = edit_user_func({'id': user_id, 'username': user.username, 'email': user.email}, db)
    if not updated_user:
        raise HTTPException(status_code=400, detail="Failed to update user")
    
    return updated_user

@router.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    result = delete_user_func(user_id, db)
    if result is False:
        raise HTTPException(status_code=404, detail="User not found")

    return {"detail": "User deleted successfully"}


