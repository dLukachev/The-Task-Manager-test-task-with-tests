from src.db.base import get_db
from src.db.models import Task
from sqlalchemy.orm import Session
from sqlalchemy import UUID

def edit_task(task_data: dict, db: Session = next(get_db())) -> Task | str:
    """
    Edit an existing task in the database.

    Args:
        task_data (dict): A dictionary containing the updated task details.
        db (Session, optional): The database session. Defaults to a new session from get_db().

    Example:
        task_data = {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "title": "Updated Task Title",
            "description": "Updated description of the task",
            "status": "in_progress"
        }

    Returns:
        Task: The updated task object.
    """
    task_id = task_data.get('id')
    if not task_id:
        return 'Task ID is required for editing a task.'

    task = db.query(Task).filter(Task.id == UUID(task_id)).first()
    if not task:
        return 'Task not found.'

    for key, value in task_data.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task