# app/routes.py
from fastapi import APIRouter, HTTPException
from app.models import WeatherRequest, WeatherResponse
from app.services import fetch_weather_data

router = APIRouter()

@router.post("/weather", response_model=WeatherResponse)
async def get_weather(request: WeatherRequest):
    """Fetch weather information for a specified city."""
    weather_data = await fetch_weather_data(request.city)
    if not weather_data:
        raise HTTPException(status_code=404, detail="City not found or API error.")
    return weather_data
