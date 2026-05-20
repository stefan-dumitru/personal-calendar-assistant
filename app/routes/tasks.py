from fastapi import APIRouter, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette import status
from fastapi import Request

from app import crud
from app.database import get_db

router = APIRouter(prefix="/tasks", tags=["tasks"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def list_tasks(request: Request, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db)

    return templates.TemplateResponse(
        request,
        "tasks.html",
        {
            "page_title": "Tasks",
            "tasks": tasks,
        },
    )


@router.post("/")
def create_task(
    title: str = Form(...),
    description: str = Form(""),
    db: Session = Depends(get_db),
):
    crud.create_task(db, title=title, description=description or None)

    return RedirectResponse(
        url="/tasks",
        status_code=status.HTTP_303_SEE_OTHER,
    )


@router.post("/{task_id}/done")
def mark_task_done(task_id: int, db: Session = Depends(get_db)):
    crud.mark_task_done(db, task_id)

    return RedirectResponse(
        url="/tasks",
        status_code=status.HTTP_303_SEE_OTHER,
    )


@router.post("/{task_id}/delete")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    crud.delete_task(db, task_id)

    return RedirectResponse(
        url="/tasks",
        status_code=status.HTTP_303_SEE_OTHER,
    )