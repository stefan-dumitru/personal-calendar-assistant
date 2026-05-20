from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Integer, String, Text

from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    due_date = Column(DateTime, nullable=True)
    estimated_minutes = Column(Integer, nullable=True)
    priority = Column(String(20), default="medium")
    status = Column(String(20), default="not_started")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))