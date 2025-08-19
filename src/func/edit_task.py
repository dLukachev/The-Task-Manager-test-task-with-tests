from uuid import UUID
from src.db.base import get_db
from src.db.models import Task
from sqlalchemy.orm import Session
from src.func.create_task import VALID_STATUSES

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
    
    if task_data.get('status') not in VALID_STATUSES:
        return 'Invalid status provided. Valid statuses are: ' + ', '.join(VALID_STATUSES)

    try:
        task_uuid = UUID(task_id)
        task = db.query(Task).filter_by(id=task_uuid).first()
        if not task:
            return 'Task not found.'

        task_data.pop('id', None)
        
        for key, value in task_data.items():
            setattr(task, key, value)

        db.commit()
        db.refresh(task)
        return task
    except ValueError:
        return 'Invalid UUID format'