from datetime import datetime

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette import status

from app import crud
from app.database import get_db

router = APIRouter(prefix="/events", tags=["events"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def list_events(request: Request, db: Session = Depends(get_db)):
    events = crud.get_events(db)

    return templates.TemplateResponse(
        request,
        "events.html",
        {
            "page_title": "Events",
            "events": events,
        },
    )


@router.post("/")
def create_event(
    title: str = Form(...),
    description: str = Form(""),
    start_datetime: str = Form(...),
    end_datetime: str = Form(...),
    location: str = Form(""),
    db: Session = Depends(get_db),
):
    crud.create_event(
        db,
        title=title,
        description=description or None,
        start_datetime=datetime.fromisoformat(start_datetime),
        end_datetime=datetime.fromisoformat(end_datetime),
        location=location or None,
    )

    return RedirectResponse(
        url="/events",
        status_code=status.HTTP_303_SEE_OTHER,
    )


@router.post("/{event_id}/delete")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    crud.delete_event(db, event_id)

    return RedirectResponse(
        url="/events",
        status_code=status.HTTP_303_SEE_OTHER,
    )