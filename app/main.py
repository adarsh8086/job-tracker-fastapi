from fastapi import FastAPI
from .database import engine
from . import models
from app.routes import users, jobs

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Personal Job Tracker API"}

app.include_router(users.router)
app.include_router(jobs.router)


