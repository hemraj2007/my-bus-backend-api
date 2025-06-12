from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from datetime import date

class BookingCreate(BaseModel):
    user_id: int
    from_location: str
    to_location: str
    seats: int
    price_per_seat: float
    travel_date: Optional[date] = None
    

    class Config:
        from_attributes = True

class BookingUpdate(BaseModel):
    from_location: Optional[str]
    to_location: Optional[str]
    seats: Optional[int]
    price_per_seat: Optional[float]

    class Config:
        from_attributes = True

class BookingResponse(BaseModel):
    id: int
    user_id: int
    from_location: str
    to_location: str
    seats: int
    price_per_seat: float
    total_price: float
    travel_date: Optional[date] = None

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
