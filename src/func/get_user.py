from src.db.base import get_db
from src.db.models import User
from sqlalchemy.orm import Session

def get_user(user_id: int, db: Session = next(get_db())) -> User:
    """
    Retrieve a user by their ID from the database.

    Args:
        user_id (int): The ID of the user to retrieve.
        db (Session, optional): The database session. Defaults to a new session from get_db().

    Returns:
        User: The user object if found, otherwise raises an exception.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError(f"User with id {user_id} does not exist.")
    return user