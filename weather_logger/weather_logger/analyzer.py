import pandas as pd
from .models import WeatherLog
from .db import SessionLocal

def fetch_data():
    session = SessionLocal()
    data = session.query(WeatherLog).all()
    session.close()
    df = pd.DataFrame([{
        'city': entry.city,
        'temperature': entry.temperature,
        'humidity': entry.humidity,
        'rainfall': entry.rainfall,
        'log_date': entry.log_date
    } for entry in data])
    return df

def generate_weekly_summary(df):
    df['log_date'] = pd.to_datetime(df['log_date'])
    summary = df.groupby(['city', pd.Grouper(key='log_date', freq='W')]).agg({
        'temperature': ['mean', 'max', 'min'],
        'humidity': 'mean',
        'rainfall': 'sum'
    }).reset_index()
    return summary

def detect_anomalies(df):
    return df[(df['temperature'] > 38) | (df['rainfall'] > 18)]
