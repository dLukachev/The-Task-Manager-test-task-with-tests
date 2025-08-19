from src.db.base import get_db
from src.db.models import Task
from sqlalchemy.orm import Session
from sqlalchemy import UUID

def create_task(task_data: dict, db: Session = next(get_db())) -> Task:
    """
    Create a new task in the database.

    Args:
        task_data (dict): A dictionary containing the task details.
        db (Session, optional): The database session. Defaults to a new session from get_db().

    Returns:
        Task: The created task object.
    """
    new_task = Task(**task_data)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task