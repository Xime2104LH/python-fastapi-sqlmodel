from sqlmodel import Session, select
from app.database.models import Task, TaskWithCategory, Category

# Con una consulta usando where y no el join
def get_join_where(session: Session):
    query = select(Task, Category).where(Task.category_id == Category.id)
    result = session.exec(query).all()
    for task, category in result:
        print("HEREE Task ", task, " Category ", category)

    return [ TaskWithCategory(task= t, category=c) for t, c in result ]

def get_join(session: Session) -> TaskWithCategory:
    query = select(Task, Category).join(Category)
    result = session.exec(query).all()
    for task, category in result:
        print("HEREE Task ", task, " Category ", category)

    return [ TaskWithCategory(task= t, category=c) for t, c in result ]

def get_join_left(session: Session) -> TaskWithCategory:
    query = select(Task, Category).join(Category, isouter=True)
    result = session.exec(query).all()

    for t, c in result:
        print("IMPRIMIENDO Task ", t, " Category ", c)

    return [ TaskWithCategory(task=t, category=c) for t, c in result ]
