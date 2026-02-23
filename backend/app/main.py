from fastapi import FastAPI
from .database import engine, Base
from . import models
from app.routes import users, jobs
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# @app.get("/")
# def root():
#     return {"message": "Personal Job Tracker API"}

app.include_router(users.router)
app.include_router(jobs.router)






origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
