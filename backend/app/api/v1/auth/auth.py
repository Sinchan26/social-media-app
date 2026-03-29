from fastapi import APIRouter, Depends, HTTPException, status
from app.services.auth_service import register_user, authenticate_user
from app.db.session import get_db
from app.schemas.user import UserCreate, UserLogin
from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db=Depends(get_db)):
    new_user=register_user(user, db)
    return{
        "user_id": str(new_user.id),
        "username": str(new_user.username),
        "email": str(new_user.email)
    }

@router.post("/login")
def login(user: UserLogin, db=Depends(get_db)):
   db_user=authenticate_user(user, db)
   token= create_access_token({"sub": str(db_user.id)})
   return {"access_token": token, "token_type": "bearer"}