from src.db.base import get_db
from src.db.models import Task
from sqlalchemy.orm import Session
from sqlalchemy import UUID

def delete_task(task_id: UUID, db: Session = next(get_db())) -> None | bool:
    """
    Delete a task from the database by its UUID.

    Args:
        task_id (UUID): The ID of the task to delete.
        db (Session, optional): The database session. Defaults to a new session from get_db().

    Raises:
        ValueError: If the task with the given ID does not exist.
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return False

    db.delete(task)
    db.commit()
    return True