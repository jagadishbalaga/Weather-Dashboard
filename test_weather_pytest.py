from weather_api import get_weather


def test_weather_data():
    data = get_weather("Hyderabad")

    assert data is not None
    assert "main" in data
    assert "temp" in data["main"]
    assert "humidity" in data["main"]

def test_invalid_city():
    data = get_weather("InvalidCity12345")

    assert data is None


def test_weather_values():
    data = get_weather("Hyderabad")

    assert data is not None

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]


    assert -50 <= temperature <= 60
    assert 0 <= humidity <= 100


from unittest.mock import patch

@patch("weather_api.requests.get")
def test_weather_mock(mock_get):

    mock_get.return_value.json.return_value = {
        "name":"Hyderabad",
        "main":{
            "temp": 30,
            "humidity":65
        }
    }

    mock_get.return_value.raise_for_status.return_value = None

    data = get_weather("Hyderabad")

    assert data["name"] == "Hyderabad"
    assert data["main"]["temp"] == 30
    assert data["main"]["humidity"] == 65


from unittest.mock import patch
import requests

@patch("weather_api.requests.get")
def test_weather_server_error(mock_get):

    mock_get.return_value.raise_for_status.side_effect = (
        requests.exceptions.HTTPError
    )

    data = get_weather("Hyderabad")

    assert data is None

@patch("weather_api.requests.get")
def test_weather_timeout(mock_get):

    mock_get.side_effect = requests.exceptions.Timeout

    data = get_weather("Hyderabad")

    assert data is None