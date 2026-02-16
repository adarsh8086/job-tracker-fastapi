# app/routes/users.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.auth import hash_password, verify_password, create_access_token
from app.schemas import UserCreate, UserLogin, Token

router = APIRouter(prefix="/users", tags=["Users"])

# Register
@router.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Check if email exists
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_user = User(
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    token = create_access_token({"user_id": db_user.id})
    return {"access_token": token, "token_type": "bearer"}

# Login
# @router.post("/login", response_model=Token)
# def login(user: UserLogin, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.email == user.email).first()
#     if not db_user or not verify_password(user.password, db_user.hashed_password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
    
#     token = create_access_token({"user_id": db_user.id})
#     return {"access_token": token, "token_type": "bearer"}



from fastapi.security import OAuth2PasswordRequestForm

@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(User.email == form_data.username).first()

    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"user_id": db_user.id})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
