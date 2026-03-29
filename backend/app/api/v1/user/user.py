from fastapi import APIRouter, Depends, status
from app.core.security import get_current_user

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/me",status_code=status.HTTP_200_OK)
def current_user_details(current_user= Depends(get_current_user))->dict:
    return {
        "id":str(current_user.id),
        "name":current_user.username,
        "email":current_user.email
    }