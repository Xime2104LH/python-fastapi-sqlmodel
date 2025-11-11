from fastapi import APIRouter
from app.schemas import Task, TasPatch

router = APIRouter(
  prefix="/api/v1",
  tags=["Tasks"]
)

tasks = []
next_id = 0

@router.get("/tasks")
async def get_tasks():
  return tasks

@router.get("/tasks/{task_id}")
async def get_task(task_id: int):
  task = None
  for x in tasks:
    if x["id"] == task_id:
      task = x
      break

  if not task:
    return {"sucess": False, "message": "Task not found", "data": []}

  return {"sucess": True, "message": "Se encontro con éxito la Task", "data": task}

@router.post("/tasks")
async def create_task(task: Task):
  new_task = task.model_dump()

  # Como lo tengo en memoria, puedo usar otra variables en memoria para
  # controlador los id
  if len(tasks) > 0:
    last_id = tasks[len(tasks) - 1]
    new_task["id"] = last_id["id"] + 1
  else:
    new_task["id"] = 1

  try:
    tasks.append(new_task)
  except:
    return {"success": False, "message": "Error trying to add a task", "data": []}
  
  return {"success": True, "message": "Se creó con éxito", "data": new_task}


@router.put("/task/{task_id}")
async def update_task(task_id: int, task: Task):
  body = task.model_dump()
  updated_task = {}

  for x in tasks:
    if(x["id"] == task_id):
      x.update(body)
      updated_task = x.copy()

  return {"success": True, "message": "Se actualizo con éxito", "data": updated_task}


@router.patch("/task/{task_id}")
async def update_task_patch(task_id: int, task: TasPatch):
  body = task.model_dump(exclude_unset=True) # este excluye los que no se enviaron en el modelo
  current_task = None

  for x in tasks:
    if x["id"] == task_id:
      current_task = x
      break
  
  if not current_task:
    return {"success":False, "message": "No se encontró la Task", "data": None}

  for key, value in body.items():
    current_task[key] = value

  return {"success": True, "message": "Se actualizo con éxito", "data": current_task}

