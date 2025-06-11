# api/routes/booking.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.database.schemas.booking import BookingResponse, BookingCreate, BookingUpdate
from api.token import get_current_user
from api.database.connection import get_db
from api.crud import booking as booking_crud

router = APIRouter()

# Create a new booking
@router.post("/bookings", response_model=BookingResponse)
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    return booking_crud.create_booking(db=db, booking=booking)

# Get all bookings
@router.get("/bookings", response_model=List[BookingResponse])
def get_bookings(db: Session = Depends(get_db)):
    bookings = booking_crud.get_all_bookings(db=db)
    return bookings

# Get booking by ID
@router.get("/bookings/user/{user_id}", response_model=List[BookingResponse])
def get_bookings_by_user(user_id: int, db: Session = Depends(get_db)):
    bookings = booking_crud.get_bookings_by_user_id(db=db, user_id=user_id)
    if not bookings:
        raise HTTPException(status_code=404, detail="No bookings found for this user")
    return bookings

# Update booking details
@router.put("/bookings/{booking_id}", response_model=BookingResponse)
def update_booking(booking_id: int, booking: BookingUpdate, db: Session = Depends(get_db)):
    updated_booking = booking_crud.update_booking(db=db, booking_id=booking_id, booking=booking)
    if not updated_booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return updated_booking

# Delete a booking entry
@router.delete("/bookings/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    deleted = booking_crud.delete_booking(db=db, booking_id=booking_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"message": "Booking deleted successfully"}

@router.get("/bookings/user/{user_id}", response_model=List[BookingResponse])
def get_bookings_by_user(user_id: int, db: Session = Depends(get_db)):
    bookings = booking_crud.get_bookings_by_user_id(db=db, user_id=user_id)
    if not bookings:
        raise HTTPException(status_code=404, detail="No bookings found for this user")
    return bookings
