
from weather_api import get_forecast
from data_processor import process_forecast_data

city = "Bhubaneswar"

forecast_data = get_forecast(city)

if forecast_data:

    daily_data = process_forecast_data(forecast_data)

    print("========== DAILY WEATHER FORECAST ==========")

    for date, row in daily_data.iterrows():

        print("\nDate:", date)
        print("Average Temperature:", row["avg_temperature"], "°C")
        print("Average Humidity:", row["avg_humidity"], "%")

else:
    print("Unable to fetch forecast data.")
