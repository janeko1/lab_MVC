from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # Typ rezerwacji (hotel, parking, itp.)
    trip_id = Column(Integer, ForeignKey('trips.id'))

    trip = relationship('Trip', back_populates='reservations')

    def __init__(self, user_name, type, trip_id):
        self.user_name = user_name
        self.type = type
        self.trip_id = trip_id
