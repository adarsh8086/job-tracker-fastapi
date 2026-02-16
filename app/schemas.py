
from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

# User schemas
class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# Job schema (optional if you want JWT-protected job routes)
class JobBase(BaseModel):
    company_name: str
    position: str
    location: str
    salary: Optional[str] = None
    status: str
    applied_date: date
    notes: Optional[str] = None

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
