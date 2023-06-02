from datetime import datetime

from pydantic import BaseModel


class TaskBase(BaseModel):
    name: str


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    completed: bool


class Task(TaskBase):
    id: int
    completed: bool
    created_at: datetime

    class Config:
        orm_mode = True
