from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Update these values as needed
DB_URL = "postgresql+psycopg2://postgres:05042003@localhost/weather_db"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def create_tables():
    from .models import WeatherLog
    Base.metadata.create_all(bind=engine)
