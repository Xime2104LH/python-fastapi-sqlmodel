
from sqlmodel import Session, select
from app.database.models import Task, TaskUpdate, Category, TaskWithCategory

"""
Escenario Anterior
Usabamos el with con session en cada endpoint/path
Escenario Actual 
Usamos una funcion generada que crea una nueva session
cada que se usa con Depends y esta al terminar cierra 
la conexión a la base de datos.
La función 
"""

# def get_session():
#     with Session(engine) as session:
#         yield session

def get_tasks(session: Session):
    statement = select(Task)
    tasks = session.exec(statement).all() 
    # el all() te da un lista de objetos y no de un iterable
    # usar también select(Task).offset(3).limit(10)
    print(tasks)
    return tasks

def get_one_task(task_id: int, session: Session):
    query = select(Task).where(Task.id == task_id)

    # result = session.exec(query)
    # Se puede hacer uso del result.one() -> lanza error si hay más de uno
    # O directo usar el session.get(Tabla, id)
    return session.exec(query).first()

def post_tasks(task: Task, session: Session):
    session.add(task)
    session.commit()
    session.refresh(task)
    print(task.id)
    return task.id
    
def put_task(task_id: int, task: Task, session: Session):
    query = select(Task).where(Task.id == task_id)
    task_found = session.exec(query).first()

    if not task_found:
        return None
    
    task_found.title = task.title
    task_found.description = task.description
    task_found.completed = task.completed

    session.add(task_found)
    session.commit()
    session.refresh(task_found)
    print("Task actualizada: ", task_found)


    return task_found

def patch_task(task_id: int, task: TaskUpdate, session: Session):
    task_current = session.get(Task, task_id)

    if not task_current:
        return None

    update_data = task.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(task_current, key, value)

    session.add(task_current)
    session.commit()
    session.refresh(task_current)
    print("Task actualizada: ", task_current)

    return task_current


def delete_task(task_id: int, session: Session):
    result = session.get(Task, task_id)

    if not result:
        return None

    session.delete(result)
    session.commit()

    return {"success": True, "message": "Eliminado con éxito"}

        


"""
    col()
    or_()
"""

