from sqlmodel import Field, SQLModel


class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    completed: bool | None = Field(default=False)
    category_id: int | None = Field(default=None, foreign_key="category.id")

class TaskUpdate(SQLModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str

class TaskWithCategory(SQLModel):
    task: Task
    category: Category | None = None

