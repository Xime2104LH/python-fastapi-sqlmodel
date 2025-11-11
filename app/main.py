from app.routes.task import todo_routes
from fastapi import FastAPI

app = FastAPI()

app.include_router(todo_routes.router)
