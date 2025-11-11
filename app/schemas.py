from pydantic import BaseModel

class Task(BaseModel):
  title: str
  description: str
  completed: bool = False

class TasPatch(BaseModel):
  title: str | None = None
  description: str | None = None
  completed: bool | None = None