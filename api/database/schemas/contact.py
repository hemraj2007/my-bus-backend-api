from pydantic import BaseModel, EmailStr

class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    message: str

class ContactResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    message: str

    class Config:
        from_attributes = True
