from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from database.database import Base

class Trip(Base):
    __tablename__ = 'trips'

    id = Column(Integer, primary_key=True)
    destination = Column(String, nullable=False)
    date = Column(Date, nullable=False)

    # Relacja z rezerwacjami
    reservations = relationship('Reservation', back_populates='trip', cascade="all, delete-orphan")

    def __init__(self, destination, date):
        self.destination = destination
        self.date = date
