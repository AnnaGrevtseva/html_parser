from app.iweather_source import IWeatherSource


def test_iweather_source():
    iws = IWeatherSource()
    assert iws is not None

    current_weather = iws.get_current_weather("moscow")
    assert isinstance(current_weather, str)
    assert current_weather == ""
