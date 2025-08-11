from sqlalchemy import Column, Integer, String, Float, Date
from .db import Base

class WeatherLog(Base):
    __tablename__ = "weather_log"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    rainfall = Column(Float, nullable=False)
    log_date = Column(Date, nullable=False)
