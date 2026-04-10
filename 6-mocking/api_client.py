from datetime import datetime
import random


def fetch_weather_data(city):
    """
    Return dict with city, temp, condition, humidity
    """
    return {
        "city": city,
        "temp": round(random.uniform(10, 30), 1),
        "condition": random.choice(["sunny", "cloudy", "rainy"]),
        "humidity": random.randint(40, 90)
    }


def fetch_forecast(city, days):
    """
    Return list of day forecasts
    """
    forecast = []
    for i in range(days):
        forecast.append({
            "day": i + 1,
            "city": city,
            "temp": round(random.uniform(10, 30), 1),
            "condition": random.choice(["sunny", "cloudy", "rainy"]),
            "humidity": random.randint(40, 90)
        })
    return forecast


def get_current_hour():
    """
    Return current hour (0-23)
    """
    return datetime.now().hour