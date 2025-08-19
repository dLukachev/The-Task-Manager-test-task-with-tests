from src.db.base import get_db
from src.db.models import User
from sqlalchemy.orm import Session

def create_user(username: str, email: str, db: Session = next(get_db())) -> User:
    """
    Create a new user in the database.

    Args:
        username (str): The username of the new user.
        email (str): The email of the new user.
        db (Session, optional): The database session. Defaults to a new session from get_db().

    Returns:
        User: The created user object.
    """

    db.query(User).filter((User.username == username) | (User.email == email)).first()
    if db.query(User).filter((User.username == username) | (User.email == email)).first():
        raise ValueError(f"User with username '{username}' or email '{email}' already exists.")

    new_user = User(username=username, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user