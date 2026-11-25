import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):

    if not API_KEY:
        print("API key is missing. Check your .env file.")
        return None

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        print("Request timed out. Try again.")
        return None

    except requests.exceptions.ConnectionError:
        print("Internet connection problem.")
        return None

    except requests.exceptions.HTTPError:
        print("API Error:", response.status_code)
        return None

    except requests.exceptions.RequestException as error:
        print("Unexpected error:", error)
        return None


def get_forecast(city):

    forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            forecast_url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        print("Forecast API Error:", error)
        return None
