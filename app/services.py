# app/services.py
import httpx
from app.models import WeatherResponse
from config import WEATHER_API_KEY, WEATHER_API_URL

async def fetch_weather_data(city: str) -> WeatherResponse:
    """Fetch weather data from OpenWeatherMap API."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                WEATHER_API_URL,
                params={
                    "q": city,
                    "appid": WEATHER_API_KEY,
                    "units": "imperial"  
                }
            )
            if response.status_code == 200:
                data = response.json()
                return WeatherResponse(
                    city=data["name"],
                    temperature=data["main"]["temp"],
                    description=data["weather"][0]["description"],
                    humidity=data["main"]["humidity"],
                    wind_speed=data["wind"]["speed"]
                )
    except Exception as e:
        print(f"Error fetching weather data: {e}")
    return None
