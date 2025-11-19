from fastapi import APIRouter, Depends
from app.database.crud_operations_category import get_categories_service, post_category_service
from sqlmodel import Session
from app.database.database_setup import engine
from app.database.models import Category

router = APIRouter(
    prefix="/api/v2",
    tags=["Category"]
)

def get_session():
    with Session(engine) as session:
        yield session

@router.get("/category")
async def get_categories(session: Session = Depends(get_session)):
    result = get_categories_service(session)

    return result

@router.post("/category")
async def post_categories(body: Category, session: Session = Depends(get_session)):
    result = post_category_service(body, session)

    return result