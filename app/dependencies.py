
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .database import get_db
from .models import User
from .auth import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_id = verify_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user
