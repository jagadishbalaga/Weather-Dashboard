from weather_api import get_weather
from data_processor import process_weather_data
from visualizations import create_weather_chart

city = "Hyderabad"

weather_data = get_weather(city)

if weather_data:

    processed_data = process_weather_data(weather_data)

    fig = create_weather_chart(processed_data)

    fig.show()

else:
    print("Unable to fetch weather data.")