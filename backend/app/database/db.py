import json
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from backend.app.config import settings

Base = declarative_base()

class UserProfileDB(Base):
    __tablename__ = "user_profiles"

    id = Column(String(64), primary_key=True, index=True)
    taste_input = Column(Text, nullable=False) # JSON
    cultural_dna = Column(Text, nullable=False) # JSON
    created_at = Column(DateTime, default=datetime.utcnow)

class SavedCityDB(Base):
    __tablename__ = "saved_cities"

    id = Column(String(64), primary_key=True, index=True)
    profile_id = Column(String(64), index=True)
    city_id = Column(String(64), nullable=False)
    notes = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

class SavedItineraryDB(Base):
    __tablename__ = "saved_itineraries"

    id = Column(String(64), primary_key=True, index=True)
    profile_id = Column(String(64), index=True)
    city_id = Column(String(64), nullable=False)
    itinerary_data = Column(Text, nullable=False) # JSON
    created_at = Column(DateTime, default=datetime.utcnow)

# Engine & Session
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
