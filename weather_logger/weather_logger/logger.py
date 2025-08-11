from .models import WeatherLog
from .db import SessionLocal
from datetime import datetime

def log_weather(city, temperature, humidity, rainfall, date=None):
    date = date or datetime.today().date()
    log = WeatherLog(
        city=city,
        temperature=temperature,
        humidity=humidity,
        rainfall=rainfall,
        log_date=date
    )
    session = SessionLocal()
    session.add(log)
    session.commit()
    session.close()
