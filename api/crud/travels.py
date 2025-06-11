from sqlalchemy.orm import Session
from api.database.models.travels import Travel
from api.database.schemas.travels import TravelCreate, TravelUpdate

# Create a new travel entry
def create_travel(db: Session, travel: TravelCreate):
    db_travel = Travel(**travel.dict())
    db.add(db_travel)
    db.commit()
    db.refresh(db_travel)
    return db_travel

# Get all travels
def get_all_travels(db: Session):
    return db.query(Travel).all()

# Get travel by ID
def get_travel_by_id(db: Session, travel_id: int):
    return db.query(Travel).filter(Travel.id == travel_id).first()

# Update travel details
def update_travel(db: Session, travel_id: int, travel: TravelUpdate):
    db_travel = db.query(Travel).filter(Travel.id == travel_id).first()
    if not db_travel:
        return None
    for key, value in travel.dict(exclude_unset=True).items():
        setattr(db_travel, key, value)
    db.commit()
    db.refresh(db_travel)
    return db_travel

# Delete travel entry
def delete_travel(db: Session, travel_id: int):
    db_travel = db.query(Travel).filter(Travel.id == travel_id).first()
    if not db_travel:
        return False
    db.delete(db_travel)
    db.commit()
    return True
