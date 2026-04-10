import api_client


def get_weather(city):
    """
    Call api_client.fetch_weather_data
    """
    try:
        return api_client.fetch_weather_data(city)
    except TimeoutError:
        return {"error": "timeout"}
    except Exception as exc:
        return {"error": str(exc).lower()}


def get_forecast(city, days):
    """
    Call api_client.fetch_forecast
    """
    return api_client.fetch_forecast(city, days)


def is_good_weather(condition):
    """
    Return True if weather is good
    """
    return condition.lower() in ["sunny", "partly cloudy"]


def get_greeting_based_on_time():
    """
    Return greeting based on current hour
    """
    hour = api_client.get_current_hour()

    if 5 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"