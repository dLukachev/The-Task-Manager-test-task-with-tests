from src.db.base import get_db
from src.db.models import User
from sqlalchemy.orm import Session
from fastapi import HTTPException

def edit_user(user_data: dict, db: Session = next(get_db())) -> User | str:
    """
    Edit an existing user in the database.

    Args:
        user_data (dict): A dictionary containing the user details.
        db (Session, optional): The database session. Defaults to a new session from get_db().

    Returns:
        User: The updated user object.
    """
    user_id = user_data.get('id')
    if not user_id:
        return 'User ID is required for editing a user.'

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return 'User not found.'

    for key, value in user_data.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user