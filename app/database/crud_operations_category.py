from sqlmodel import select, Session
from app.database.models import Category

def get_categories_service(session: Session):
    query = select(Category)
    result = session.exec(query).all()
    print(result)
    return result


def post_category_service(category: Category, session: Session):
    session.add(category)
    session.commit()
    session.refresh(category)

    print(category.id)

    return { "success": True, "message": "Se creó con éxito", "data": category}
