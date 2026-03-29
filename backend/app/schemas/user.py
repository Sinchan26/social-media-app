from pydantic import BaseModel, EmailStr,Field

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50,description="user name must be between 3 and 50 characters")
    email: EmailStr= Field(..., description="user email must be a valid email address")
    password: str = Field(..., min_length=8, max_length=12,description="password must be between 12 and 15 characters")

class UserLogin(BaseModel):
    email: EmailStr= Field(..., description="user email must be a valid email address")
    password: str = Field(..., min_length=8, max_length=12,description="password must be between 12 and 15 characters")    