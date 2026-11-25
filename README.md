# 🌤️ Weather Dashboard

## Dashboard Preview

![Weather Dashboard](screenshots/weather_dashboard.png)

A real-time Weather Dashboard built using Python and Streamlit with the OpenWeather API.

## Features
- Search weather by city name.
- Display current temperature and feels-like temperature.
- Show humidity, wind speed, and atmospheric pressure.
- Display weather conditions.
- Show a 5-day weather forecast.
- Calculate average daily temperature and humidity.
- Automated testing using Pytest.

## Technologies Used
- Python
- Streamlit
- Pandas
- Requests
- OpenWeather API
- Pytest

## Project Structure
- `app.py` – Main Streamlit application.
- `weather_api.py` – Fetches weather data from the API.
- `data_processor.py` – Processes weather and forecast data.
- `visualizations.py` – Visualization functions.
- `requirements.txt` – Required Python packages.
- `test_*.py` – Automated test files.

## Installation

1. Clone the repository.
2. Install the required packages:

   `pip install -r requirements.txt`

3. Create a `.env` file and add your OpenWeather API key:

   `OPENWEATHER_API_KEY=your_api_key`

4. Run the application:

   `python -m streamlit run app.py`

## Note
This project is developed for learning and educational purposes.
