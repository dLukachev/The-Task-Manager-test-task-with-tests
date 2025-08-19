from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from src.db.base import get_db
from src.func.create_task import create_task as create_task_func
from src.func.get_task import get_task as get_task_func
from src.func.edit_task import edit_task as edit_task_func
from src.func.delete_task import delete_task as delete_task_func
from src.db.schema import TaskCreate, Task
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    task_data = task.model_dump()
    create_task_result = create_task_func(task_data, db)
    if not create_task_result:
        raise HTTPException(status_code=400, detail="Task creation failed")
    return create_task_result

@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: UUID, db: Session = Depends(get_db)):
    task = get_task_func(task_id, db) # type: ignore
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=Task)
def edit_task(task_id: UUID, task: TaskCreate, db: Session = Depends(get_db)):
    task_data = task.model_dump()
    task_data['id'] = str(task_id)
    updated_task = edit_task_func(task_data, db)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@router.delete("/tasks/{task_id}", response_model=dict)
def delete_task(task_id: UUID, db: Session = Depends(get_db)):
    result = delete_task_func(task_id, db) # type: ignore
    if result is False:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted successfully"}