from fastapi import APIRouter, Depends
from app.database.database_setup import engine
from sqlmodel import Session
from app.database.crud_operations_tasks import get_tasks, post_tasks, get_one_task, put_task, patch_task, delete_task, get_join
from app.database.models import Task, TaskUpdate

router = APIRouter(
    prefix="/api/v2",
    tags=["Task SQLModel"]
)

def get_session():
    with Session(engine) as session:
        yield session


@router.get("/tasks")
async def get(session: Session = Depends(get_session)):
    tasks = get_tasks(session)
    return tasks
    
@router.post("/tasks")
async def post(task: Task, session: Session = Depends(get_session)):
    validate = Task.model_validate(task)
    return post_tasks(validate, session)

@router.get("/tasks/{task_id}")
async def get_one(task_id: int, session: Session = Depends(get_session)):
    task = get_one_task(task_id, session)
    return task

@router.put("/tasks/{task_id}")
async def put(task_id: int, task:  Task, session: Session = Depends(get_session)):
    task_updated = put_task(task_id, task, session)
    
    return task_updated

@router.patch("/tasks/{task_id}")
async def patch(task_id: int, task: TaskUpdate, session: Session = Depends(get_session)):
    task_updated = patch_task(task_id, task, session)

    return task_updated

@router.delete("/tasks/{task_id}")
async def delete(task_id: int, session: Session = Depends(get_session)):
    result = delete_task(task_id, session)

    return result