from weather_api import get_weather
from data_processor import process_weather_data

city = "Hyderabad"

weather_data = get_weather(city)

if weather_data:

    processed_data = process_weather_data(weather_data)

    print("========== WEATHER REPORT ==========")

    for key, value in processed_data.items():
        print(f"{key}: {value}")

else:
    print("Unable to fetch weather data.")