
from weather_api import get_weather, get_forecast
from data_processor import process_weather_data, process_forecast_data
import streamlit as st

st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="🌤️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0b1220, #172b46);
    color: white;
}

h1, h2, h3, p, label {
    color: white !important;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

.weather-card {
    background: rgba(255, 255, 255, 0.08);
    padding: 25px;
    border-radius: 18px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    margin-bottom: 15px;
}

div[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.09);
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 22px;
    border-radius: 16px;
    min-height: 125px;
}

div[data-testid="stMetricLabel"] {
    color: #b8c7dc !important;
}

div[data-testid="stMetricValue"] {
    color: white !important;
    font-size: 27px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# Dashboard heading
st.title("🌤️ Weather Dashboard")
st.write("Your personal live weather overview")

st.divider()

# City search
city = st.text_input(
    "Search City",
    value="Bhubaneswar",
    placeholder="Enter city name..."
)

if st.button("Get Weather"):

    if city.strip():

        weather_data = get_weather(city)

        forecast_data = get_forecast(city)

        if weather_data:

            data = process_weather_data(weather_data)

            if forecast_data:
                daily_forecast = process_forecast_data(forecast_data)
            else:
                daily_forecast = None

            st.subheader(f"Weather in {data['city']}")

            # Current weather card
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(120deg, #1e4168, #284f78);
                    padding: 30px;
                    border-radius: 20px;
                    margin: 20px 0;
                ">
                    <p style="color:#c5d9ef; font-size:18px;">
                        CURRENT WEATHER
                    </p>
                    <h1 style="color:white; font-size:65px; margin:5px 0;">
                        {data['temperature']}°C
                    </h1>
                    <h3 style="color:white; margin:0;">
                        {data['city']}
                    </h3>
                    <p style="color:#c5d9ef; font-size:18px;">
                        {data['description'].title()}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Weather metrics
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("🌡️ Temperature", f"{data['temperature']} °C")

            with col2:
                st.metric("🤗 Feels Like", f"{data['feels_like']} °C")

            with col3:
                st.metric("💧 Humidity", f"{data['humidity']} %")

            col4, col5, col6 = st.columns(3)

            with col4:
                st.metric("🌬️ Wind Speed", f"{data['wind_speed']} m/s")

            with col5:
                st.metric("⏱️ Pressure", f"{data['pressure']} hPa")

            with col6:
                st.metric("☁️ Condition", data['description'].title())

            # 5-day forecast
            st.divider()

            st.subheader("📅 5-Day Weather Forecast")

            if daily_forecast is not None:

                forecast_display = daily_forecast[
                    ["date", "avg_temperature", "avg_humidity"]
                ].rename(columns={
                    "date": "Date",
                    "avg_temperature": "Temperature (°C)",
                    "avg_humidity": "Humidity (%)"
                })

                st.dataframe(
                    forecast_display,
                    use_container_width=True,
                    hide_index=True
                )