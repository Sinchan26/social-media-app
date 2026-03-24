from app.schemas.user import UserCreate, UserLogin
from app.models.user import User
from app.core.security import hash_password, verify_password
from fastapi import HTTPException, status

def register_user(user: UserCreate,db):
    if(db.query(User).filter(User.email == user.email).first()):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
    hashed_password = hash_password(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_email(email: str,db):
    return db.query(User).filter(User.email == email).first()

def authenticate_user(user: UserLogin,db):
    db_user = get_user_by_email(user.email,db)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password" )
    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    return db_user