from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from dependencies.database import Base


class Task(Base):
    __tablename__ = "Tasks"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())
