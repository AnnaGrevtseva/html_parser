from app.weather_manager import WeatherManager


def test_get_temperature_success(weather_source_good):
    wm = WeatherManager(weather_source_good)
    assert wm.get_temperature('moscow') == '-5°'


def test_get_temperature_error(weather_source_bad):
    wm = WeatherManager(weather_source_bad)
    assert wm.get_temperature('moscow') is None
