from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import main

from . import models, schemas

tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])


@tasks_router.get("/", response_model=list[schemas.Task], status_code=200)
def get_tasks(db: Session = Depends(main.get_db)):
    tasks = db.query(models.Task).offset(0).limit(100).all()
    return tasks


@tasks_router.get("/{task_id}", response_model=schemas.Task, status_code=200)
def get_task_by_id(task_id: int, db: Session=Depends(main.get_db)):
    task = db.query(models.Task).filter(models.Task.id==task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@tasks_router.post("/", response_model=schemas.Task, status_code=201)
def create_task(task: schemas.TaskCreate, db: Session=Depends(main.get_db)):
    task = models.Task(name=task.name)
    db.add(task)
    db.commit()
    db.refresh(task)
    task = db.query(models.Task).filter(models.Task.id==task.id).first()
    return task


@tasks_router.put("/{task_id}", response_model=schemas.Task, status_code=200)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session=Depends(main.get_db)):
    query_task = db.query(models.Task).filter(models.Task.id==task_id)
    if not query_task.first():
        raise HTTPException(status_code=404, detail="Task not found")
    query_task.update(values={"name": task.name, "completed": task.completed}, synchronize_session="evaluate")
    db.commit()
    return query_task.first()


@tasks_router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session=Depends(main.get_db)):
    db.query(models.Task).filter(models.Task.id==task_id).delete()
    db.commit()
    return
