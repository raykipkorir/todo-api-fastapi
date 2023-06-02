from fastapi import FastAPI

from apps.tasks import models
from dependencies.database import SessionLocal, engine

# create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from apps.tasks.routers import tasks_router

app.include_router(router=tasks_router)
