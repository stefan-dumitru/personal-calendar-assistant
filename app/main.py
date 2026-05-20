from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app import models
from app.database import Base, engine
from app.routes import views, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Personal Calendar Assistant")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(views.router)
app.include_router(tasks.router)