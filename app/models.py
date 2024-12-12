# app/models.py
from pydantic import BaseModel

class WeatherRequest(BaseModel):
    city: str

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    description: str
    humidity: int
    wind_speed: float
