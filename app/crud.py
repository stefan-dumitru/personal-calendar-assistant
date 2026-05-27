from sqlalchemy.orm import Session

from app import models


def get_tasks(db: Session):
    return db.query(models.Task).order_by(models.Task.created_at.desc()).all()


def create_task(
    db: Session,
    title: str,
    description: str | None = None,
    due_date=None,
    estimated_minutes: int | None = None,
    priority: str = "medium",
):
    task = models.Task(
        title=title,
        description=description,
        due_date=due_date,
        estimated_minutes=estimated_minutes,
        priority=priority,
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


def get_events(db: Session):
    return db.query(models.Event).order_by(models.Event.start_datetime.asc()).all()


def create_event(
    db: Session,
    title: str,
    description: str | None,
    start_datetime,
    end_datetime,
    location: str | None,
):
    event = models.Event(
        title=title,
        description=description,
        start_datetime=start_datetime,
        end_datetime=end_datetime,
        location=location,
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return event


def delete_event(db: Session, event_id: int):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()

    if not event:
        return None

    db.delete(event)
    db.commit()

    return event