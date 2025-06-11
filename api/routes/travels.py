from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from api.database.schemas.travels import TravelResponse, TravelCreate, TravelUpdate
from api.database.connection import get_db
from api.crud import travels as travels_crud

router = APIRouter()

# Get all travels
@router.get("/all", response_model=List[TravelResponse])
def get_all_travels(db: Session = Depends(get_db)):
    travels = travels_crud.get_all_travels(db)
    if not travels:
        raise HTTPException(status_code=404, detail="No travels found.")
    return travels

# Get a specific travel by ID
@router.get("/{travel_id}", response_model=TravelResponse)
def get_travel_by_id(travel_id: int, db: Session = Depends(get_db)):
    travel = travels_crud.get_travel_by_id(db, travel_id)
    if not travel:
        raise HTTPException(status_code=404, detail="Travel not found.")
    return travel

# Create a new travel entry
@router.post("/add", response_model=TravelResponse)
def add_travel(travel: TravelCreate, db: Session = Depends(get_db)):
    return travels_crud.create_travel(db, travel)

# Update travel entry
@router.put("/update/{travel_id}", response_model=TravelResponse)
def update_travel(travel_id: int, travel: TravelUpdate, db: Session = Depends(get_db)):
    updated_travel = travels_crud.update_travel(db, travel_id, travel)
    if not updated_travel:
        raise HTTPException(status_code=404, detail="Travel not found.")
    return updated_travel

# Delete travel entry
@router.delete("/delete/{travel_id}")
def delete_travel(travel_id: int, db: Session = Depends(get_db)):
    deleted = travels_crud.delete_travel(db, travel_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Travel not found.")
    return {"message": "Travel deleted successfully."}
