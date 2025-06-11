from sqlalchemy.orm import Session
from api.database.models.booking import Booking
from api.database.schemas.booking import BookingCreate, BookingUpdate

# Create a new booking entry
def create_booking(db: Session, booking: BookingCreate):
    total_price = booking.seats * booking.price_per_seat  # Calculate total price
    db_booking = Booking(**booking.dict(), total_price=total_price)  # Set the calculated total_price
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

# Get all bookings
def get_all_bookings(db: Session):
    return db.query(Booking).all()

# Get booking by ID
def get_bookings_by_user_id(db: Session, user_id: int):
    return db.query(Booking).filter(Booking.user_id == user_id).all()

# Update booking details
def update_booking(db: Session, booking_id: int, booking: BookingUpdate):
    db_booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if db_booking:
        for key, value in booking.dict(exclude_unset=True).items():
            if value is not None:
                setattr(db_booking, key, value)
        
        # Recalculate total_price when updating
        if booking.seats is not None and booking.price_per_seat is not None:
            db_booking.total_price = db_booking.seats * db_booking.price_per_seat

        db.commit()
        db.refresh(db_booking)
        return db_booking
    return None

# Delete booking entry
def delete_booking(db: Session, booking_id: int):
    db_booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if db_booking:
        db.delete(db_booking)
        db.commit()
        return True
    return False

def get_bookings_by_user_id(db: Session, user_id: int):
    return db.query(Booking).filter(Booking.user_id == user_id).all()