from src.db.base import get_db
from src.db.models import Task
from sqlalchemy.orm import Session

VALID_STATUSES = ['create', 'in work', 'closed']

def create_task(task_data: dict, db: Session = next(get_db())) -> Task | None:
    """
    Create a new task in the database.

    Args:
        task_data (dict): A dictionary containing the task details.
        db (Session, optional): The database session. Defaults to a new session from get_db().

    Returns:
        Task: The created task object.
    """

    if task_data.get('status') not in VALID_STATUSES:
        return None

    new_task = Task(**task_data)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task