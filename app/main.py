from app.routes.task import todo_routes, tasks_routes
from fastapi import FastAPI
from app.database.database_setup import create_db_and_tables
from contextlib import asynccontextmanager
from app.routes.category import category_routes

# Este se esta quedando obsoleto por lo que usaremos lifespan mejor
# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(" 🟢 Starting up")
    create_db_and_tables()
    yield
    print(" 🔴 Sutting down")

def get_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(tasks_routes.router)
    app.include_router(category_routes.router)
    return app

app = get_app()

