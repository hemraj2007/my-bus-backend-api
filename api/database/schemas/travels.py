from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TravelResponse(BaseModel):
    id: int
    image: str
    from_location: str
    to_location: str
    time: datetime
    seats: int
    price: float

    class Config:
        from_attributes = True

class TravelCreate(BaseModel):
    image: str
    from_location: str
    to_location: str
    time: datetime
    seats: int
    price: float

class TravelUpdate(BaseModel):
    image: str
    from_location: Optional[str] = None
    to_location: Optional[str] = None
    time: Optional[datetime] = None
    seats: Optional[int] = None
    price: Optional[float] = None
