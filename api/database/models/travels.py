# api/database/models.py
from sqlalchemy import Column, Integer, String, DateTime, Float
from api.database.connection import Base

class Travel(Base):
    __tablename__ = 'travels'

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String(100), nullable=False)
    from_location = Column(String(100), nullable=False)
    to_location = Column(String(100), nullable=False)
    time = Column(DateTime, nullable=False)
    seats = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
