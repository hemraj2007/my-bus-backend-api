from sqlalchemy.orm import Session
from api.database.models.contact import Contact
from api.database.schemas.contact import ContactCreate

def create_contact(db: Session, contact: ContactCreate):
    new_contact = Contact(
        name=contact.name,
        email=contact.email,
        message=contact.message
    )
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact

def get_all_contacts(db: Session):
    return db.query(Contact).all()
