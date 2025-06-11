from pydantic import BaseModel, EmailStr
from typing import Optional

# Create User Schema (used in registration)
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    mob_number: str
    role: str = "user" 

# Login Schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Update User Schema
class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    mob_number: Optional[str]
    password: Optional[str] = None

    class Config:
        from_attributes = True

# Response Schema (used in API responses)
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    mob_number: str
    role: str = "user"

    class Config:
        from_attributes = True

# Password Update Schema (without current password)
class PasswordUpdate(BaseModel):
    new_password: str
    confirm_password: str


class UserProfileUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    mob_number: Optional[str]

    class Config:
        from_attributes = True