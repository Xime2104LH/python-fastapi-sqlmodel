from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.database.database_setup import engine
from app.database.crud_task_category import get_join, get_join_left, get_join_where

router = APIRouter(
    prefix="/api/v2",
    tags=["Task With Categories"]
)

def get_session():
    with Session(engine) as session:
        yield session


@router.get("/tasks/category")
async def get_task_categories(session: Session = Depends(get_session)):
    result = get_join_where(session)

    return result

@router.get("/tasks/category-join")
async def get_task_categories_join(session: Session = Depends(get_session)):
    result = get_join(session)

    return result

@router.get("/tasks/category-join-left")
async def get_task_categories_join_left(session: Session = Depends(get_session)):
    result = get_join_left(session)

    return result
