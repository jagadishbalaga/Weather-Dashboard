
import pandas as pd


def process_weather_data(weather_data):

    processed_data = {
        "city": weather_data["name"],
        "temperature": weather_data["main"]["temp"],
        "feels_like": weather_data["main"]["feels_like"],
        "humidity": weather_data["main"]["humidity"],
        "pressure": weather_data["main"]["pressure"],
        "wind_speed": weather_data["wind"]["speed"],
        "description": weather_data["weather"][0]["description"]
    }

    return processed_data


def process_forecast_data(forecast_data):

    records = forecast_data["list"]

    df = pd.DataFrame(records)

    df["date"] = pd.to_datetime(df["dt_txt"]).dt.date

    daily_forecast = df.groupby("date").agg(
        temperature=("main", lambda x: [
            item["temp"] for item in x
        ]),
        humidity=("main", lambda x: [
            item["humidity"] for item in x
        ])
    )

    daily_forecast["avg_temperature"] = (
        daily_forecast["temperature"].apply(
            lambda x: round(sum(x) / len(x), 1)
        )
    )

    daily_forecast["avg_humidity"] = (
        daily_forecast["humidity"].apply(
            lambda x: round(sum(x) / len(x), 1)
        )
    )

    # Convert date index into a normal column
    daily_forecast = daily_forecast.reset_index()

    # Format date as day-month-year
    daily_forecast["date"] = pd.to_datetime(
        daily_forecast["date"]
    ).dt.strftime("%d-%m-%Y")

    return daily_forecast
