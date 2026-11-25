import plotly.graph_objects as go


def create_weather_chart(weather_data):

    labels = ["temperature","feels like"]

    values = [
        weather_data["temperature"],
        weather_data["feels_like"]
    ]


    fig = go.Figure(
        data=[
            go.Bar(
                x=labels,
                y=values,
                text=values,
                textposition="auto"
            )
        ]
    )

    fig.update_layout(
        title="Temperature comparision",
        xaxis_title="weather metrics",
        yaxis_title="temperature (°C)"
    )

    return fig