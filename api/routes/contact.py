from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from api.database.schemas.contact import ContactCreate, ContactResponse
from api.database.connection import get_db
from api.crud import contact as contact_crud

router = APIRouter()

@router.post("/", response_model=ContactResponse)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    return contact_crud.create_contact(db, contact)

@router.get("/get all", response_model=List[ContactResponse])
def get_contacts(db: Session = Depends(get_db)):
    return contact_crud.get_all_contacts(db)
