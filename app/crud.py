from sqlalchemy.orm import Session

from app import models


def get_tasks(db: Session):
    return db.query(models.Task).order_by(models.Task.created_at.desc()).all()


def create_task(db: Session, title: str, description: str | None = None):
    task = models.Task(
        title=title,
        description=description,
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def mark_task_done(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        return None

    task.status = "done"
    db.commit()
    db.refresh(task)

    return task


def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        return None

    db.delete(task)
    db.commit()

    return task