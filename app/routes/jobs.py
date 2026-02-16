# app/routes/jobs.py
from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import get_current_user
from app.models import Job
from app.schemas import Job as JobSchema
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import JobCreate, Job as JobSchema

router = APIRouter(prefix="/jobs", tags=["Jobs"])

# @router.get("/", response_model=list[JobSchema])
# def read_jobs(current_user = Depends(get_current_user), db: Session = Depends(get_db)):
#     # Only return jobs for the logged-in user
#     return db.query(Job).filter(Job.user_id == current_user.id).all()



@router.get("/{job_id}", response_model=JobSchema)
def get_single_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    job = db.query(Job).filter(
        Job.id == job_id,
        Job.user_id == current_user.id
    ).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return job


# pagination
@router.get("/", response_model=list[JobSchema])
def read_jobs(
    skip: int = 0,
    limit: int = 2,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return (
        db.query(Job)
        .filter(Job.user_id == current_user.id)
        .offset(skip)
        .limit(limit)
        .all()
    )




# 🔹 Create Job
@router.post("/", response_model=JobSchema)
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    new_job = Job(
        company_name=job.company_name,
        position=job.position,
        location=job.location,
        salary=job.salary,
        status=job.status,
        applied_date=job.applied_date,
        notes=job.notes,
        user_id=current_user.id   # imp
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job




@router.put("/{job_id}", response_model=JobSchema)
def update_job(
    job_id: int,
    updated_data: JobCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    # Ownership check
    if job.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    for key, value in updated_data.model_dump().items():
        setattr(job, key, value)

    db.commit()
    db.refresh(job)

    return job







@router.delete("/{job_id}")
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    #  Ownership check
    if job.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    db.delete(job)
    db.commit()

    return {"message": "Job deleted successfully"}
