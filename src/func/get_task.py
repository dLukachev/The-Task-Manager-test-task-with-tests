from src.db.base import get_db
from src.db.models import Task
from sqlalchemy import UUID
from sqlalchemy.orm import Session

def get_task(task_id: UUID, db: Session = next(get_db())) -> Task | None:
    """
    Retrieve a task by its UUID from the database.

    Args:
        task_id (UUID): The ID of the task to retrieve.
        db (Session, optional): The database session. Defaults to a new session from get_db().

    Returns:
        Task: The task object if found, otherwise raises an exception.
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None
    return task