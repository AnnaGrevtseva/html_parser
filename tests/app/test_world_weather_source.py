import requests
from app.iweather_source import IWeatherSource
from app.world_weather_source import WorldWeatherSource


def test_world_weather_source():
    wws = WorldWeatherSource()
    assert wws is not None
    assert isinstance(wws, IWeatherSource)

    current_weather = wws.get_current_weather("moscow")
    assert isinstance(current_weather, str)
