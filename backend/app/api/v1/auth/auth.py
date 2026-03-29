from fastapi import APIRouter, Body, Depends, HTTPException, status
from jose import ExpiredSignatureError, JWTError, jwt
from app.services.auth_service import register_user, authenticate_user
from app.db.session import get_db
from app.schemas.user import UserCreate, UserLogin
from app.core.security import create_access_token,create_refresh_token
import os

router = APIRouter(prefix="/auth", tags=["auth"])
SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

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
   token_r= create_refresh_token({"sub": str(db_user.id)})
   return {"access_token": token,"refresh_token":token_r, "token_type": "bearer"}

@router.post("/refresh")
def refresh_token(refresh_token: str = Body(...)):
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])

        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid token type")

        user_id = payload.get("sub")

        new_access_token = create_access_token({"sub": user_id})

        return {
            "access_token": new_access_token,
            "token_type": "bearer"
        }

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Refresh token expired")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")