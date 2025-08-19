from src.db.base import get_db
from src.db.models import User
from sqlalchemy.orm import Session
from fastapi import HTTPException

def delete_user(user_id: int, db: Session = next(get_db())) -> bool:
    """
    Delete a user from the database by their ID.

    Args:
        user_id (int): The ID of the user to delete.
        db (Session, optional): The database session. Defaults to a new session from get_db().

    Returns:
        bool: True if the user was deleted successfully, False if the user was not found.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return False

    db.delete(user)
    db.commit()
    return True