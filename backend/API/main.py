from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.ingestion.fetch_weather import fetch_data
from backend.processing.clean_transform import data_forming

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Weather API is running. Use /weather/{city}"}


@app.get("/weather/{city}")
def get_weather_city(city: str):

    city = city.strip().lower()

    # 1. Fetch directly from weather API
    raw_data = fetch_data(city)

    if raw_data is None:
        return {
            "error": "Unable to fetch weather data. Check the city name or API key."
        }

    # 2. Clean and transform API data
    df = data_forming(raw_data)

    # 3. Return processed weather data
    return {
        "source": "weather_api",
        "city": city,
        "data": df.to_dict(orient="records")
    }