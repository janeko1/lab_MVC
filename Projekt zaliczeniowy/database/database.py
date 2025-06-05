from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URI  # Importowanie URI bazy danych


# Tworzenie silnika bazodanowego
engine = create_engine(DATABASE_URI, echo=True)

# Definicja bazowej klasy dla modeli
Base = declarative_base()

# Tworzenie sesji dla operacji na bazie danych
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Funkcja inicjalizująca bazę danych
def init_db():
    from models.trip import Trip
    from models.reservation import Reservation
    
    Base.metadata.create_all(bind=engine)
